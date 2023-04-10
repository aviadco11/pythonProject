import ast

with open('dict.txt') as f:
    data = f.read()
    d = ast.literal_eval(data)

print(f"name: {d['name']}, age: {d['age']}")