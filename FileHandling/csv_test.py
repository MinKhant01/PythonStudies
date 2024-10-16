"""
import csv

with open("dict_data.csv",'r',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Age: {row['Age']}")

with open('data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('data.csv','r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)

"""

"""
import csv

data = [
    {'Name': 'Alice', 'Age': 99},
    {'Name': 'Bob', 'Age': 98},
    {'Name': 'Charlie', 'Age':97}
]

with open('dict_data.csv','a',newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name','Age'])
    #writer.writeheader()

    for row in data:
        writer.writerow(row)

data = [
    ['apple', 'banana', 'cherry']
    ['car', 'train', 'ship']
]
with open('data.txt', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for row in data:
    writer.writerow(row)
"""

    