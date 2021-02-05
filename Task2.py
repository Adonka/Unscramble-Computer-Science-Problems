"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#Dictionary can check if the number already exits or not. Then we can count by the size of dictionary.
num_dic = {}

#Numbers are shown in the first two columns(j), so for-loop can go over the first two elments in two lists (list = i)
for i in range(len(calls)):
    j = 0
    while(j < 2):
        if calls[i][j] not in num_dic:
            num_dic[calls[i][j]] = int(calls[i][3])
        else:
            num_dic[calls[i][j]] += int(calls[i][3])
        j += 1

#Find the max value from the value of the num_dic dictionary as well as the key.
max_val = max(num_dic.values())
max_key = max(num_dic, key=num_dic.get)

#Print the output.
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, max_val))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

