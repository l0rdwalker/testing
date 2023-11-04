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

data = json.loads(read_file_as_string(os.path.join(filePath,'app.slack.com.har')))
data = data['log']['entries']
y = 1
for x in range(0,len(data)):
    if ('conversations.history' in data[x]['request']['url']):
        content = data[x]['response']['content']['text']
        write_file(os.path.join(filePath,'processedData'),str(content),y)
        y += 1
