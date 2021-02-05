"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#Initialize two dictionaries.
num_dic = {}
Bangalore_dic = {}

#Iterate the calls records from the imported calls list to store the each number into two dictionaries.
for i in range(len(calls)):
    j = 0
    while(j < 2):
        if calls[i][j] not in num_dic:
            num_dic[calls[i][j]] = 1
            if "(080)" in calls[i][j]:
                Bangalore_dic[calls[i][j]] = 1

        else:
            num_dic[calls[i][j]] += 1
            if "(080)" in calls[i][j]:
                Bangalore_dic[calls[i][j]] += 1
        j += 1

#Create the list of keys from the Bangalore_dic dictionary.
Bangalore_list = Bangalore_dic.keys()

#Calculate the sum from each dictionary
sum_Bang = sum(Bangalore_dic.values())
sum_val = sum(num_dic.values())

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
