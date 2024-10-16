import json

#json.load(file)        -> reads JSON data from a file
#json.dump(obj, file)   -> writes JSON data to a file
#json.loads(s)          -> parses JSON data from a string
#json.dumps(obj)        -> converts a Python object to a JSON string


"""
with open('test_data.json','r') as file:
    data = json.load(file)
    print(data)

data = {"name": "Bob", "age": 24}
with open('test_data.json', 'a') as file:
    json.dump(data, file)
"""

invalid_json_string = '{name: "Alice", age: 30}'
valid_json_string = '{"name": "Alice", "age": 30}'

try:
    new_data = json.loads(valid_json_string)
    print(new_data)
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")

my_data = {
    "name": "Alice",
    "age": 30,
    "greet": "Hello, World!"
}

try:
    json_string = json.dumps(my_data)
    print(json_string)
except TypeError as e:
    print(f"TypeError: {e}")