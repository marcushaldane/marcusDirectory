#
print("===============================================================")

def getMag(num):
	size = 1
	while(num>0):
		num=num//10
		size=size*10
	return size

def number_reversal(num):
# Bust a move right here
	size = getMag(num)
	multiple = size
	
	rtnval = 0
	while(num>0):
		# print(num)
		newnum = num%10 
		rtnval += (newnum*multiple)
		num=num//10
		multiple=multiple//10
		#print(newnum)

	rtnval=rtnval//10
	return rtnval
   
#function tests
a=number_reversal(1231234)
print("a: " + str(a))
print("===============================================================")

