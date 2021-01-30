"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#Dictionary can check if the number already exits or not. Then we can count by the size of dictionary.
num_dic = {}
count = 0
#Numbers are shown in the first two columns(j), so for-loop can go over the first two elments in two lists (each list = i)
for i in range(len(texts)):
    j = 0
    while(j < 2):
        for number in texts[i][j]:
            if number not in num_dic:
                num_dic[number] = 1
            else:
                num_dic[number] += 1
            j += 1
for i in range(len(calls)):
    j = 0
    while(j < 2):
        for number in calls[i][j]:
            if number not in num_dic:
                num_dic[number] = 1
            else:
                num_dic[number] += 1
            j += 1
#asigned the size of the dictionary
count = len(num_dic)

print("There are {} different telephone numbers in the records.".format(count))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
