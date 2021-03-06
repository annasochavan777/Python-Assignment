#########################################################################################################
# Write a recursive program which accept number from user and return its factorial.
# Input : 5
# Output : 120
# Author : Annaso Chavan
#########################################################################################################

fact = 0
no = 0
# calculate factorial of number 
def FactorialNum():
	global fact
	global no
	while no!=0:
		if fact == 0:
			fact = no
		else:
			fact = fact * no
		no -= 1
		FactorialNum()
	else:
		return fact

# calculate factorial of number using local variable 
def FactorialNumLocalVariable(no,fact):
	while no!=0:
		if fact == 0:
			fact = no
		else:
			fact = fact * no
		no -= 1
		FactorialNumLocalVariable(no,fact)
	else:
		return fact
		
def main():
	global no
	no = int(input("please enter Number :"))
	print("Sum of digits are : ",FactorialNum())
	
	number = int(input("please enter Number :"))
	print("Sum of digits are using local variable : ",FactorialNumLocalVariable(number,0))
	
# code starter 
if __name__ == "__main__":
	main()