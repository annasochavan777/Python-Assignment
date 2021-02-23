###########################################################################################
# Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True
# Author : Annaso Chavan
###########################################################################################

# function to check number is divisible by 5
def NumberIsDivisible(num):
	if num % 5 == 0:
		return True # return true if number is divisible by 5
	else:
		return False # return false if not divisible by 5

def main():
	num = int(input("please enter number :")) # take input from user
	print(NumberIsDivisible(num)) # call NumberIsDivisible function
	
# code starter 
if __name__ == "__main__":
	main()