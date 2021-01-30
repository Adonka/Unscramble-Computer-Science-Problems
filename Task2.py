"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
most_spent_number = ""
#Numbers are shown in the first two columns(j), so for-loop can go over the first two elments in two lists (list = i)
for i in range(len(calls)):
    j = 0
    while(j < 2):
        for number in calls[i][j]:
            if number not in num_dic:
                num_dic[number] = int(calls[i][3])
            else:
                num_dic[number] += int(calls[i][3])
            j += 1

number_list = num_dic.keys()
time_list = num_dic.values()

most_spent_number = num_dic.keys().index(max(num_dic.values()))

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(most_spent_number, num_dic[most_spent_number]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

