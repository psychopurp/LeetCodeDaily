import os
import re
from typing import List, Optional, Set
import requests
import json

session = requests.Session()
user_agent = r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"


class Problem:
    def __init__(
        self, id: int, title: str, difficulty: str, tags: List[str], url: str
    ) -> None:
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.tags = tags
        self.url = url
        self.solved = False

    def markdown_table(self) -> str:
        tags = []
        for tag in self.tags:
            tags.append(tag["name"])
        link = "| [{}. {}]({})  |  ✅  |   {}    |".format(
            self.id, self.title, self.url, ""
        )
        return link

    def markdown_li(self) -> str:
        solved = "x" if self.solved else " "
        link = "* [{}] [{}. {}]({})\n".format(solved, self.id, self.title, self.url)
        return link


def fetch_problems(problem_title: str) -> Optional[Problem]:
    slug = problem_title
    url = "https://leetcode.com/graphql"
    params = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": slug},
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

    json_data = json.dumps(params).encode("utf8")
    headers = {
        "User-Agent": user_agent,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/problems/" + slug,
    }

    try:
        resp = session.post(url, data=json_data, headers=headers, timeout=10)
        question = resp.json()["data"]["question"]
        raw_url = "https://leetcode-cn.com/problems/{}/".format(slug)
        problem = Problem(
            int(question["questionFrontendId"]),
            question["questionTitle"],
            question["difficulty"],
            question["topicTags"],
            raw_url,
        )
        return problem
    except:
        print("encounter an error while fetching {}".format(slug))
        return None


def render_md(file: str):
    slug = re.compile("problems/[^/\n\)]*")

    lines: List[str] = read_md(file)
    solved = get_solved(".")
    visited = set()

    def get_title(s: str) -> str:
        params = s.split("/")
        return params[-1]

    output: List[str] = []
    lines.append("\n")
    problems: List[Problem] = []
    for line in lines:
        slugs: List[str] = slug.findall(line)
        if len(slugs) == 1:
            title = get_title(slugs[0])
            problem = fetch_problems(title)
            if problem:
                if problem.id in visited:
                    print(f"duplicate problems:{problem.id}")

                visited.add(problem.id)
                if problem.id in solved:
                    problem.solved = True
                problems.append(problem)
            else:
                print("error problem {}".format(slugs))

        else:
            if problems:
                problems.sort(key=lambda x: x.id)
                p = map(lambda x: x.markdown_li(), problems)
                output.extend(p)
                problems.clear()
            output.append(line)

    with open("README.md", "w") as f:
        f.writelines(output)
    print(solved.difference(visited))
    print("done!")


def get_solved(dir: str) -> Set[int]:
    problem = re.compile("[0-9]*\.[^\u4E00-\u9FFF]+\.py")
    solved = set()

    for root, _, files in os.walk(dir):
        problems: List[str] = []
        for file in files:
            if problem.match(file):
                problems.append(file)
                solved.add(int(file.split(".")[0]))
        if problems:
            print(root, len(problems))
    print("total solved : {}".format(len(solved)))
    return solved


def read_md(file: str) -> List[str]:
    lines: List[str] = []
    with open(file) as f:
        lines = f.readlines()
    return lines


def main():
    render_md("./README.md")
    exit(0)


if __name__ == "__main__":
    main()
