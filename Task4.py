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

#Set can check if the number already exits or not. 
text_senders = set()
callers = set()
text_recievers = set()
call_recievers = set()
num_call_marketing = set()

#Iterate calls and texts lists to store the output into two dictionaries.
for i in range(len(texts)):
    j = 0
    
    
    while(j < 2):
        if j == 0 and texts[i][j] not in text_senders:
            text_senders.add(texts[i][j])
        else:
            text_recievers.add(texts[i][j])
        j += 1

for i in range(len(calls)):
    j = 0
    
    while(j < 2):
        if j == 0 and calls[i][j] not in callers:
            callers.add(texts[i][j])
        else:
            call_recievers.add(texts[i][j])
        j += 1
            
#Iterate the callers set to add the key which does not exist in incoming call and texts.
for outgoing_call in callers:
    if outgoing_call not in text_recievers: 
        if outgoing_call not in text_senders:
            if outgoing_call not in call_recievers:
                num_call_marketing.add(outgoing_call)

marketing = list(num_call_marketing)

#Print the the output of Marketing number set.
print("These numbers could be telemarketers: {}".format(marketing))

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

