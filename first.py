
print "this is my first python program"


# Variable & Unpacking Example

my_variable = [1,4.2,True]
int,float,bool = my_variable
print type(int)
print type (float)
print type(bool)

'''And also we are using Type for recognize the value Type'''
#Packing 
def varibale(int,float,bool):
	print int,float,bool
arg = 1,4.2,True
varibale(*arg)

	

