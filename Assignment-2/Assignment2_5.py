#####################################################################
# Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number
# Author : Annaso Chavan
#####################################################################

# function to check whether number is prime or not 
def IsPrimeNumber(no):
	counter = 0
	for i in range(2,no,1): # range(start, stop, step)
		if no % i == 0:
			counter += 1
		if counter > 0: # if counter incremented by 1 means number is not a prime number so no need to triverse loop further so break the loop early 
			break
	return counter == 0

def main():
	no = int(input("please enter no :"))
	result = IsPrimeNumber(no)
	
	if result:
		print("It is Prime Number")
	else:
		print("It is not Prime Number")
		
# code starter 
if __name__ == "__main__":
	main()