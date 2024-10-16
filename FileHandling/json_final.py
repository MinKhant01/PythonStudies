import json

with open('test_data.json', 'r') as file:
    data = json.load(file)
    for entity in data:
        for key, value in entity.items():
            print(f"{key}: {value}")