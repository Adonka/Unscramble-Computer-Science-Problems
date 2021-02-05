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
num_texts = {}
num_calls = {}
num_call_marketing = set()

for i in range(len(texts)):
    j = 0
    
    for number in texts[i][j]:
        while(j < 2):
            if number not in num_texts:
                num_texts[number] = 1
            else:
                num_texts[number] += 1
            j += 1
print(num_texts)
for i in range(len(calls)):
    j = 0
    while(j < 2):
        for number in calls[i][j]:
            if number not in num_calls and number != calls[i][1]:
                num_calls[number] = 1
                j += 1
            elif number in num_calls:
                num_calls[number] += 1
                j += 1
            else:
                j += 1

for key in num_calls.items():
    if key not in num_texts:
        num_call_marketing.add(key)

print("These numbers could be telemarketers: " + str(num_call_marketing))

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

