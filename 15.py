import datetime
from time import sleep
import requests
def check_if_url_up(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        return True
    return False

print(check_if_url_up("https://76o12.com"))

print(datetime.datetime.now())
sleep(3)
print(datetime.datetime.now())