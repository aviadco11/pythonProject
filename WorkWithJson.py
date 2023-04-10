import json
import requests

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
# we see is define as dict
print(type(data))

# define as a string
json_string = json.dumps(data)
print(type(json_string))
print(json_string)
print(json.dumps(data))
print(json.dumps(data, indent=4))

# write json to file
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


# load() to load from file
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(type(data))
print(data)
print(data["president"])


json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
# loads() to load from string
data = json.loads(json_string)
print(type(data))
print(data)
print(data["researcher"]["name"])



response = requests.get("https://jsonplaceholder.typicode.com/todos")

todos = response.json()
print("requests:")
print(todos)

for o1 in todos:
    print(o1["userId"])


data = {
    "president": {
        "name": "(a , b)",
        "species": "Betelgeusian"
    }
}

load_data = json.dumps(data)
tt = json.loads(load_data)
tu = tt["president"]["name"]
print(tt["president"]["name"])

# dict
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print(type(student_id))
print(student_id[111])

# set
student_id = {"Eric", "Kyle", "Butters"}
print(type(student_id))
