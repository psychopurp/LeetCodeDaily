
from typing import List
import requests
import json

session = requests.Session()
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'


class Problems:
    def __init__(self, id: int, title: str, difficulty: str, tags: List[str], url: str) -> None:
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.tags = tags
        self.url = url

    def markdown_table(self) -> str:
        tags = []
        for tag in self.tags:
            tags.append(tag["name"])
        link = "|  | [{}. {}]({})  | {}| {}  | ✅      |".format(
            self.id, self.title, self.url, self.difficulty, "")
        return link

    def markdown_li(self) -> str:
        link = "* [x] [{}. {}]({})".format(
            self.id, self.title, self.url)
        return link


def get_problem_by_url(raw_url: str) -> Problems:
    print("processing : {}".format(raw_url))
    splt = raw_url.split("/")
    slug = splt[-1] if splt[-1] else splt[-2]
    url = "https://leetcode.com/graphql"
    params = {'operationName': "getQuestionDetail",
              'variables': {'titleSlug': slug},
              'query': '''query getQuestionDetail($titleSlug: String!) {
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
        }'''
              }

    json_data = json.dumps(params).encode('utf8')

    headers = {'User-Agent': user_agent, 'Connection':
               'keep-alive', 'Content-Type': 'application/json',
               'Referer': 'https://leetcode.com/problems/' + slug}

    resp = session.post(url, data=json_data, headers=headers, timeout=10)

    content = resp.json()

    # 题目详细信息
    question = content['data']['question']

    print(question)

    problem = Problems(int(question["questionId"]), question["questionTitle"],
                       question["difficulty"], question["topicTags"], raw_url)
    return problem


def read_data():
    import re
    # findall() 查找匹配正则表达式的字符串

    with open("data") as f:
        url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+.*', f.read())
        return url


if __name__ == "__main__":
    links = read_data()
    problems: List[Problems] = []
    for link in links:
        problems.append(get_problem_by_url(link))

    problems.sort(key=lambda x: x.id)
    with open("res", "w+") as f:

        for problem in problems:
            f.write("{}\n".format(problem.markdown_li()))
