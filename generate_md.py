import os
import re
import json
import logging
import argparse
from typing import List, Optional, Set, Dict, Any
from dataclasses import dataclass
from pathlib import Path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import concurrent.futures
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Constants
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
LEETCODE_API_URL = "https://leetcode.com/graphql"
LEETCODE_CN_BASE_URL = "https://leetcode-cn.com/problems/{}/"


@dataclass
class Problem:
    """Represents a LeetCode problem with its metadata."""
    id: int
    title: str
    difficulty: str
    tags: List[Dict[str, str]]
    url: str
    solved: bool = False

    def get_tag_names(self) -> List[str]:
        """Extract tag names from tag objects."""
        return [tag.get("name", "") for tag in self.tags if isinstance(tag, dict)]

    def markdown_table(self) -> str:
        """Generate markdown table row for the problem."""
        status = "✅" if self.solved else "❌"
        tags_str = ", ".join(self.get_tag_names())
        return f"| [{self.id}. {self.title}]({self.url}) | {status} | {self.difficulty} | {tags_str} |"

    def markdown_li(self) -> str:
        """Generate markdown list item for the problem."""
        checkbox = "x" if self.solved else " "
        return f"* [{checkbox}] [{self.id}. {self.title}]({self.url})\n"


class LeetCodeAPI:
    """API client for fetching LeetCode problem information."""

    def __init__(self):
        self.session = self._create_session()
        self.cache: Dict[str, Problem] = {}

    def _create_session(self) -> requests.Session:
        """Create a session with retry strategy and proper headers."""
        session = requests.Session()

        # Retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Default headers
        session.headers.update(
            {
                "User-Agent": USER_AGENT,
                "Content-Type": "application/json",
            }
        )

        return session

    def fetch_problem(
        self, problem_slug: str, use_cache: bool = True
    ) -> Optional[Problem]:
        """Fetch a problem from LeetCode API with caching support."""
        if use_cache and problem_slug in self.cache:
            logger.debug(f"Using cached data for problem: {problem_slug}")
            return self.cache[problem_slug]

        logger.info(f"Fetching problem: {problem_slug}")

        query_params = {
            "operationName": "getQuestionDetail",
            "variables": {"titleSlug": problem_slug},
            "query": """query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    questionTitle
                    questionTitleSlug
                    content
                    difficulty
                    stats
                    similarQuestions
                    categoryTitle
                    topicTags {
                        name
                        slug
                    }
                }
            }""",
        }

        try:
            json_data = json.dumps(query_params).encode("utf8")
            headers = {
                "Referer": f"https://leetcode.com/problems/{problem_slug}",
            }

            response = self.session.post(
                LEETCODE_API_URL, data=json_data, headers=headers, timeout=10
            )
            response.raise_for_status()

            data = response.json()
            question_data = data.get("data", {}).get("question")

            if not question_data:
                logger.warning(f"No question data found for: {problem_slug}")
                return None

            problem = Problem(
                id=int(question_data["questionFrontendId"]),
                title=question_data["questionTitle"],
                difficulty=question_data["difficulty"],
                tags=question_data["topicTags"],
                url=LEETCODE_CN_BASE_URL.format(problem_slug),
            )

            # Cache the result
            if use_cache:
                self.cache[problem_slug] = problem

            return problem

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error while fetching {problem_slug}: {e}")
            return None
        except (KeyError, ValueError, json.JSONDecodeError) as e:
            logger.error(f"Data parsing error for {problem_slug}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error while fetching {problem_slug}: {e}")
            return None

    def fetch_problems_batch(
        self, problem_slugs: List[str], max_workers: int = 5
    ) -> List[Optional[Problem]]:
        """Fetch multiple problems concurrently."""
        logger.info(
            f"Fetching {len(problem_slugs)} problems with {max_workers} workers"
        )

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all fetch tasks
            future_to_slug = {
                executor.submit(self.fetch_problem, slug): slug
                for slug in problem_slugs
            }

            results = []
            for future in concurrent.futures.as_completed(future_to_slug):
                slug = future_to_slug[future]
                try:
                    result = future.result()
                    results.append((slug, result))
                except Exception as e:
                    logger.error(f"Error processing {slug}: {e}")
                    results.append((slug, None))

        # Sort results by original order
        slug_to_result = dict(results)
        return [slug_to_result.get(slug) for slug in problem_slugs]


class MarkdownGenerator:
    """Main class for generating and updating README.md from LeetCode problems."""

    def __init__(self, readme_path: str = "README.md", max_workers: int = 5):
        self.readme_path = Path(readme_path)
        self.api = LeetCodeAPI()
        self.max_workers = max_workers
        self.url_pattern = re.compile(r"problems/[^/\n\)]*")

    def extract_problem_slug(self, url_match: str) -> str:
        """Extract problem slug from URL pattern match."""
        return url_match.split("/")[-1]

    def get_solved_problems(self, directory: str = ".") -> Set[int]:
        """Scan directory for solved problems based on filename pattern."""
        problem_pattern = re.compile(r"[0-9]*\.[^\u4E00-\u9FFF]+\.py")
        solved = set()

        for root, _, files in os.walk(directory):
            problems_in_dir = []
            for file in files:
                if problem_pattern.match(file):
                    problems_in_dir.append(file)
                    try:
                        problem_id = int(file.split(".")[0])
                        solved.add(problem_id)
                    except (ValueError, IndexError):
                        logger.warning(
                            f"Could not extract problem ID from filename: {file}"
                        )

            if problems_in_dir:
                logger.info(f"Found {len(problems_in_dir)} solved problems in {root}")

        logger.info(f"Total solved problems: {len(solved)}")
        return solved

    def read_readme(self) -> List[str]:
        """Read the current README.md file."""
        try:
            with open(self.readme_path, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            logger.warning(f"README file not found at {self.readme_path}")
            return []
        except Exception as e:
            logger.error(f"Error reading README file: {e}")
            return []

    def write_readme(self, lines: List[str]) -> None:
        """Write updated content to README.md."""
        try:
            with open(self.readme_path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            logger.info(f"Successfully updated {self.readme_path}")
        except Exception as e:
            logger.error(f"Error writing README file: {e}")
            raise

    def process_problems_in_section(self, problems: List[Problem]) -> List[str]:
        """Convert a list of problems to markdown format."""
        if not problems:
            return []

        # Sort problems by ID
        problems.sort(key=lambda x: x.id)
        return [problem.markdown_li() for problem in problems]

    def generate_readme(self) -> None:
        """Main method to generate updated README.md."""
        logger.info("Starting README generation process")

        lines = self.read_readme()
        if not lines:
            logger.error("No content to process")
            return

        solved_problems = self.get_solved_problems(".")
        visited_problem_ids = set()
        output_lines = []
        current_section_problems = []

        # Add a newline to trigger processing of the last section
        lines.append("\n")

        # Collect all problem slugs first for batch processing
        all_problem_slugs = []
        for line in lines:
            url_matches = self.url_pattern.findall(line)
            if len(url_matches) == 1:
                slug = self.extract_problem_slug(url_matches[0])
                all_problem_slugs.append(slug)

        # Fetch all problems in batch
        logger.info(f"Fetching {len(all_problem_slugs)} problems...")
        fetched_problems = self.api.fetch_problems_batch(
            all_problem_slugs, self.max_workers
        )
        slug_to_problem = dict(zip(all_problem_slugs, fetched_problems))

        # Process lines and build output
        for line in lines:
            url_matches = self.url_pattern.findall(line)

            if len(url_matches) == 1:
                slug = self.extract_problem_slug(url_matches[0])
                problem = slug_to_problem.get(slug)

                if problem:
                    if problem.id in visited_problem_ids:
                        logger.warning(f"Duplicate problem found: {problem.id}")

                    visited_problem_ids.add(problem.id)

                    # Mark as solved if found in filesystem
                    if problem.id in solved_problems:
                        problem.solved = True

                    current_section_problems.append(problem)
                else:
                    logger.error(f"Failed to fetch problem: {slug}")
            else:
                # End of section or non-problem line
                if current_section_problems:
                    # Add processed problems to output
                    problem_lines = self.process_problems_in_section(
                        current_section_problems
                    )
                    output_lines.extend(problem_lines)
                    current_section_problems.clear()

                # Add the current line (section header, empty line, etc.)
                output_lines.append(line)

        # Write updated content
        self.write_readme(output_lines)

        # Report statistics
        unvisited_solved = solved_problems.difference(visited_problem_ids)
        if unvisited_solved:
            logger.warning(f"Solved problems not found in README: {unvisited_solved}")

        logger.info("README generation completed successfully!")


# Legacy function for backward compatibility
def fetch_problems(problem_title: str) -> Optional[Problem]:
    """Legacy function for backward compatibility."""
    api = LeetCodeAPI()
    return api.fetch_problem(problem_title)


# Legacy functions for backward compatibility
def render_md(file: str):
    """Legacy function - use MarkdownGenerator.generate_readme() instead."""
    logger.warning(
        "render_md() is deprecated. Use MarkdownGenerator.generate_readme() instead."
    )
    generator = MarkdownGenerator(readme_path=file)
    generator.generate_readme()


def get_solved(directory: str) -> Set[int]:
    """Legacy function - use MarkdownGenerator.get_solved_problems() instead."""
    logger.warning(
        "get_solved() is deprecated. Use MarkdownGenerator.get_solved_problems() instead."
    )
    generator = MarkdownGenerator()
    return generator.get_solved_problems(directory)


def read_md(file: str) -> List[str]:
    """Legacy function - use MarkdownGenerator.read_readme() instead."""
    logger.warning(
        "read_md() is deprecated. Use MarkdownGenerator.read_readme() instead."
    )
    generator = MarkdownGenerator(readme_path=file)
    return generator.read_readme()


def create_argument_parser() -> argparse.ArgumentParser:
    """Create command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate and update LeetCode problems in README.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Update README.md in current directory
  %(prog)s --readme my_readme.md    # Specify custom README file
  %(prog)s --workers 10             # Use 10 concurrent workers
  %(prog)s --verbose                # Enable debug logging
        """,
    )

    parser.add_argument(
        "--readme",
        "-r",
        type=str,
        default="README.md",
        help="Path to README.md file (default: README.md)",
    )

    parser.add_argument(
        "--workers",
        "-w",
        type=int,
        default=5,
        help="Number of concurrent workers for API requests (default: 5)",
    )

    parser.add_argument(
        "--directory",
        "-d",
        type=str,
        default=".",
        help="Directory to scan for solved problems (default: current directory)",
    )

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    parser.add_argument("--quiet", "-q", action="store_true", help="Only show errors")

    return parser


def main():
    """Main entry point with command line argument support."""
    parser = create_argument_parser()
    args = parser.parse_args()

    # Configure logging level
    if args.quiet:
        logging.getLogger().setLevel(logging.ERROR)
    elif args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Create generator and run
        generator = MarkdownGenerator(readme_path=args.readme, max_workers=args.workers)

        start_time = time.time()
        generator.generate_readme()
        end_time = time.time()

        logger.info(f"Process completed in {end_time - start_time:.2f} seconds")

    except KeyboardInterrupt:
        logger.info("Process interrupted by user")
        return 1
    except Exception as e:
        logger.error(f"Process failed: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
