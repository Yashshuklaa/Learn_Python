import re
import json
import os
import sys
import random

# '''Dict'''


cricket = {'sachin':'batsman','dhoni':'keeper','ishant':'bowler','ashvin':'spiner'}
print (cricket['ishant'])#find value
del (cricket['dhoni'])#delete key from dict 
cricket['ishant'] = 'allrounder'#rename diffrent value for key in dict 
print len(cricket)#lenght of dict
# Use (GET) For Getting value
print (cricket.get('dhoni'))#use get for getting value
print cricket.keys()#get keys form dict
print cricket.values()#get values form dict

print('Yash')

					

					