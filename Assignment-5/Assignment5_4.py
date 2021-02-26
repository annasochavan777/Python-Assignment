#########################################################################################################
# Write a recursive program which accept number from user and return summation of its digits.
# Input : 879
# Output : 24
# Author : Annaso Chavan
#########################################################################################################

sum = 0
no = 0 
def SumOfDigits():
	global sum,no
	while no!=0:
		sum += int(no % 10)
		no = int(no/10)
		SumOfDigits()
	else:
		return sum;

def main():
	global no
	number = int(input("please enter Number :"))
	no = number
	print("Sum of digits are : ",SumOfDigits())
	
# code starter 
if __name__ == "__main__":
	main()