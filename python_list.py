
import re
import json
import random
import sys

'''List'''

emp_list = ['yash','aayush','ajay','harshit','Sam']

# index
print emp_list[0]
print emp_list[1]
# sort
emp_list.sort()
print emp_list
# reverse
emp_list.reverse()
print emp_list

# append
emp_list.append('Yashwant')
print emp_list

# insert
emp_list.insert(0,'subhash')
print emp_list
# remove
emp_list.remove('ajay')
print emp_list
# append List into List
sal_list = ['1000','5000','8000','100']

add_list = (emp_list,sal_list)
# added here list in list in var
print add_list
# added here list in to one list
add_list = emp_list + sal_list
print add_list


# loop in 2 list and finding one list
for i in range(len(sal_list)):
	print sal_list
for i in range(len(emp_list)):
	print emp_list

# we can find the length of list
print len(sal_list) #find the len of list
print max(sal_list) #find the max len in the list
print min(sal_list) #find the min len in the list

