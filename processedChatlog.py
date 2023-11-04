import json
import os
from datetime import datetime, timedelta
import shutil
import csv

def read_file_as_string(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

def write_file(dir, data, i):
    with open(os.path.join(dir,f'{i}.txt'), 'a') as file:
        file.write(data)

def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

filePath = os.path.dirname(os.path.abspath(__file__))
dataDir = os.path.join(os.path.join(filePath, 'processedData'), 'chatlog.txt')
imageDirectpry = os.path.join(filePath,'images')
outputDirectory = os.path.join(filePath,'output')

make_dir(outputDirectory)

data = json.loads(read_file_as_string(dataDir))
teamMembers = ['Allen', 'Pratul', 'Alexis', 'William', 'Ayushmaan', 'Fawaz', 'Zeeshan']

for teamMember in teamMembers:
    memberDirectory = os.path.join(outputDirectory,teamMember)
    make_dir(memberDirectory)

    messages = ''
    start_week_current = datetime.now().date() + timedelta(days=1)
    weekIndex = 12

    while (weekIndex >= 0):
        end_week_current = start_week_current + timedelta(days=6)
        messages += f'\n\n{start_week_current.strftime("%Y-%m-%d %H:%M:%S")} week: {weekIndex}\n'
        for x in reversed(range(-1,len(data)-1)):
            if (teamMember in data[x]['user']):
                messageTime = datetime.utcfromtimestamp(data[x]['time']).date()
                if (start_week_current < messageTime < end_week_current):
                    imageID = str(data[x]["time"]).replace('.','')
                    imageDirectory = os.path.join(imageDirectpry,f'{imageID}.png')

                    if os.path.isfile(imageDirectory):
                        shutil.move(imageDirectory,memberDirectory)
                    else:
                        imageID = 'n/a'

                    messages += f'{data[x]["user"]} ({imageID}): {data[x]["message"]}\n'

        weekIndex -= 1
        start_week_current = start_week_current - timedelta(weeks=1)

    write_file(memberDirectory,messages,f'{teamMember}Messages')