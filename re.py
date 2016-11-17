import re 




'''Regulare expression is a powerfull function'''
'''split function will produce a list '''
'''ctrl+B for using run the program''' 


print (re.split(r'\s*','here are some word'))
print (re.split(r'(\s*)','here are some word'))

print (re.split(r'[a-f]','tajhdfkjahskjfhkjashkfnvcmbhfkjehkvj'))

'''[a-f] find the range of chr'''
''' /d - digits
	/D - non-digits
	/s -space 
	/S - non-space
'''

