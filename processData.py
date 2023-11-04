import os
import json

def read_file_as_string(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

def write_file(dir,data,i):
    with open(os.path.join(dir,f'{i}.txt'), 'w') as file:
        file.write(data)

filePath = os.path.dirname(os.path.abspath(__file__))

y = 1
cache = {}
for i in range(1,160):
    specificPath = os.path.join(filePath,f'{i}.txt')
    data = json.dumps(json.loads(read_file_as_string(specificPath))['messages'])

    if not (data in cache):
        cache[data] = True
        write_file(os.path.join(filePath,'processedData'),data,y)
        y += 1
