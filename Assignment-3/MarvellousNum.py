#########################################################
# MarvellousNum module
#########################################################


# function to check whether number is prime or not 
def ChkPrime(no):
	counter = 0
	for i in range(2,no,1): # range(start, stop, step)
		if no % i == 0:
			counter += 1
		if counter > 0: # if counter incremented by 1 means number is not a prime number so no need to triverse loop further so break the loop early 
			break
	return counter == 0

# function to add two number
def Add(no1,no2):
	return no1 + no2