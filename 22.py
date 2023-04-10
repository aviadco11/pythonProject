# can use exceptions from some modules
import requests
from requests.exceptions import InvalidURL

try:
    response = requests.get("safasdfsdaf")
except InvalidURL:
    print("invalid url")
