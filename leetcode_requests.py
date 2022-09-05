import requests
import json
from requests.exceptions import HTTPError

LEETCODE_URL = "https://leetcode.com"
LEETCODE_ENDPOINT = "https://leetcode.com/graphql"
QOTD_QUERY = """query questionOfToday {
    activeDailyCodingChallengeQuestion {
        date
        userStatus
        link
        question {
            acRate
            difficulty
            freqBar
            frontendQuestionId: questionFrontendId
            isFavor
            paidOnly: isPaidOnly
            status
            title
            titleSlug
            hasVideoSolution
            hasSolution
            topicTags {
                name
                id
                slug
            }
        }
    }
}"""

RANDOM_QUESTION_QUERY = """query randomQuestion($categorySlug: String, $filters: QuestionListFilterInput) {
  randomQuestion(categorySlug: $categorySlug, filters: $filters) {
    titleSlug
  }
}"""

RANDOM_QUESTION_VARIABLES = """{
  "categorySlug": "",
  "filters": {}
}"""

RANDOM_QUESTION_DIFFICULTY_VARIABLES = {
  "categorySlug": "",
  "filters": {
    "difficulty": ""
  }
}

RANDOM_QUESTION_TAG_VARIABLES = {
  "categorySlug": "",
  "filters": {
    "tags": [
      ""
    ]
  }
}   

def get_leetcode_daily():
    try:
        post_request = requests.post(LEETCODE_ENDPOINT, json={"query": QOTD_QUERY})
        if post_request.status_code == 200:
            # whole response body
            #print(json.dumps(get_request.json(), indent=2))

            problem_url = post_request.json().get("data").get("activeDailyCodingChallengeQuestion").get("link")
            qotd_link = LEETCODE_URL + problem_url
            return qotd_link

    except HTTPError as e:
        print(e.read().decode())

def get_random_question():
    try:
        post_request = requests.post(LEETCODE_ENDPOINT, json={"query": RANDOM_QUESTION_QUERY, "variables" : RANDOM_QUESTION_VARIABLES})
        if post_request.status_code == 200:
            problem_url = post_request.json().get("data").get("randomQuestion").get("titleSlug")
            random_question_url = LEETCODE_URL + "/problems/" + problem_url
            return random_question_url

    except HTTPError as e:
        print(e.read().decode())

def get_random_difficulty(difficulty):
    try:
        variables = RANDOM_QUESTION_DIFFICULTY_VARIABLES
        variables["filters"]["difficulty"] = difficulty
        post_request = requests.post(LEETCODE_ENDPOINT, json={"query": RANDOM_QUESTION_QUERY, "variables" : variables})
        if post_request.status_code == 200:
            problem_url = post_request.json().get("data").get("randomQuestion").get("titleSlug")
            random_question_url = LEETCODE_URL + "/problems/" + problem_url
            return random_question_url

    except HTTPError as e:
        print(e.read().decode())

def get_random_tag(tag):
    try:
        variables = RANDOM_QUESTION_TAG_VARIABLES
        variables["filters"]["tags"][0] = tag
        post_request = requests.post(LEETCODE_ENDPOINT, json={"query": RANDOM_QUESTION_QUERY, "variables" : variables})
        if post_request.status_code == 200:
            problem_url = post_request.json().get("data").get("randomQuestion").get("titleSlug")
            random_question_url = LEETCODE_URL + "/problems/" + problem_url
            return random_question_url

    except HTTPError as e:
        print(e.read().decode())
