import requests
response = requests.post("http://127.0.0.1:5001/whatismyname")
actual = "saved new cars"
expected = response.text
assert actual == expected