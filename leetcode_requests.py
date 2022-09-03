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
