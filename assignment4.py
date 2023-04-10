import string

import requests
from requests.exceptions import InvalidURL
import json
import random
from selenium import webdriver


def test_github_api(url):
    try:
        response = requests.get(url)
        y = json.loads(response.content)
        response.close()
        if len(y) > 5:
            print("URL: {0} has above than 5 repos".format(url))
        else:
            print("URL: {0} has less than 5 repos".format(url))
        assert len(y) > 5
    except InvalidURL:
        print("invalid url")
    except BaseException as e:
        print("something went wrong")
        print(e.args)


test_github_api("https://api.github.com/users/avielb/repos")


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


def test_agify_api(url):
    for i in range(3):
        name = get_random_string(3)
        try:
            verify_url = url + "=" + name
            print(verify_url)
            response = requests.get(verify_url)
            age = response.json()["age"]
            response.close()
            if 0 <= age <= 120:
                print("AGE: {0} is between 1-120".format(age))
            else:
                print("AGE: {0} is not between 1-120".format(age))
        except BaseException as e:
            print("something went wrong")
            print(e.args)


test_agify_api("https://api.agify.io/?name")


def test_universities_api(url):
    try:
        response = requests.get(url)
        con = json.loads(response.content)
        response.close()
        cnt = 0
        for j in con:
            if j["country"] == "Israel":
                cnt += 1
        if cnt > 4:
            print("israel has at least 5 universities")
        else:
            print("israel has less than 5 universities")

    except BaseException as e:
        print("something went wrong")
        print(e.args)
    assert cnt > 4


test_universities_api("http://universities.hipolabs.com/search?country=Israel")

def test_title_url(url, text_cmp):
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.title
    print(title)
    assert title == text_cmp

test_title_url("https://www.ycombinator.com/", "Y Combinator")
test_title_url("https://hub.docker.com/", "Docker Hub Container Image Library | App Containerization")
