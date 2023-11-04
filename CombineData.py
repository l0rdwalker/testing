import os
import json
import re
import queue

def read_file_as_string(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

def write_file(dir,data,i):
    with open(os.path.join(dir,f'{i}.txt'), 'w') as file:
        file.write(data)

filePath = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(filePath,'processedData')
data = []

userMap = {
    'U05L4LAUD5M':'Allen Burias',
    'U05L4KQPT7Z':'Pratul Singh Raghava',
    'U05LK6ZMJAW':'Alexis Lee',
    'U05M8TJDA48':'William Walker',
    'U05LG93SWA1':'Ayushmaan Tomar',
    'U05LML08Z1A':'Fawaz Al Khreisha',
    'U05LK3UFA75':'Zeeshan Ansari',
    'U05M1QLH2KF':'@Yanxiao Li'
}

messageCount = {
    'Allen Burias':{'num':0,'len':0},
    'Pratul Singh Raghava':{'num':0,'len':0},
    'Alexis Lee':{'num':0,'len':0},
    'William Walker':{'num':0,'len':0},
    'Ayushmaan Tomar':{'num':0,'len':0},
    'Fawaz Al Khreisha':{'num':0,'len':0},
    'Zeeshan Ansari':{'num':0,'len':0},
    '@Yanxiao Li':{'num':0,'len':0}
}

def replaceNames(string:str):
    #{'message': '<@U05L4KQPT7Z> <@U05...tance test', 'user': 'Ayushmaan Tomar'}
    string = string.replace('\n',' ')
    for key, value in userMap.items():
        substring_to_check = f'<@{key}>'
        replacement = value
        string = re.sub(substring_to_check, replacement, string)
    return string

totalCharacters = 0
totalMessages = 0

for x in reversed(range(1,27)):
    local = json.loads(read_file_as_string(os.path.join(filePath,f'{x}.txt')))
    for y in range(0,len(local['messages'])):
        try:
            if not ('Yanxiao Li' in userMap[local['messages'][y]['user']]):
                messageCount[userMap[local['messages'][y]['user']]]['num'] += 1
                messageCount[userMap[local['messages'][y]['user']]]['len'] += len(local['messages'][y]['text'])
                totalMessages += 1
                totalCharacters += len(local['messages'][y]['text'])

            #textMessage = replaceNames(local['messages'][y]['text'])
            #timeSpamp = float(local['messages'][y]['ts'])
            #hashCode = hash(textMessage)
            #if (hashCode < 0):
            #    hashCode = hashCode * -1
            #message = {'id':hashCode, 'message':textMessage,'user':userMap[local['messages'][y]['user']],'time':timeSpamp}
        except Exception as e:
            #print(local['messages'][y]['text'])
            print(local['messages'][y]['user'])
        #data.append(message)

priorityQueueNum = queue.PriorityQueue()
priorityQueueLen = queue.PriorityQueue()
for key,value in messageCount.items():
    priorityQueueNum.put((value["num"], key))
    priorityQueueLen.put((value["len"], key))
    print(f'\nUser: {key} totalMessages: {value["num"]/totalMessages} totalCharactersSent: {value["len"]/totalCharacters}')

print('\nMessageQTY')
count = 9
while not (priorityQueueNum.qsize() == 0):
    count -= 1
    itemNum = priorityQueueNum.get()
    print(f'{itemNum[1]}: {count}     Percentage: {(itemNum[0]/totalMessages)*100}')

print('\nMessageQTY')
count = 9
while not (priorityQueueLen.qsize() == 0):
    count -= 1
    itemLen = priorityQueueLen.get()
    print(f'{itemLen[1]}: {count}     Percentage: {(itemLen[0]/totalCharacters)*100}')

print(f'totalMessages:{totalMessages} totalCharactes:{totalCharacters}')
#write_file(filePath,json.dumps(data),'chatlog')
