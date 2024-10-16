import os

file_path = "./test_dir"
os.mkdir(file_path)
os.chdir(file_path)
with open("test_file.txt","a") as file:
    pass