"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#Initialize sets and lists.
callers = []
call_recievers = []
Bangalore_set = set()
Bangalore_recievers_set = set()
Bangalore_call_set = set()
count = 0


#Iterate the calls records from the imported calls list to store the each number into two dictionaries.
for i in range(len(calls)):
    j = 0
    while(j < 2):
        if "(" and ")" in calls[i][j]:
            f = calls[i][j].find(")")
            Bangalore_set.add(calls[i][j][1:f])
            if "(080)" in calls[i][j] and j == 0:
                callers.append(calls[i][j])
                if "(080)" in calls[i][1]:
                    count += 1
            elif "(080)" in calls[i][j] and j == 1:
                call_recievers.append(calls[i][j])
        elif " " in calls[i][j]:
            spliter = calls[i][j].split(" ")
            Bangalore_set.add(spliter[0])
        elif calls[i][j].startswith("140"):
            Bangalore_call_set.add("140")  
        j += 1

#Create the list of keys from the Bangalore_set set.
Bangalore_list = list(Bangalore_set)
Bangalore_list = sorted(Bangalore_list)

#Calculate the sums from counter and length of the list
sum_Bang = count
sum_val = len(callers)

#Calculate the percentage from the sum.
percentage = int((sum_Bang/sum_val) * 100)

#Print the output.
print("The numbers called by people in Bangalore have codes: {}".format(Bangalore_list))
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
