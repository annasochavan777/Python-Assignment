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

# below function is not working calculate factorial of number 
def FactorialNumLocalVariable(no):
	global fact
	print("fact :", fact)
	print("no :", no)
	while no!=0:
		if fact == 0:
			fact = no
		else:
			fact = fact * no
		no -= 1
		FactorialNumLocalVariable(no)
	else:
		return fact
		
def main():
	global no
	no = int(input("please enter Number :"))
	print("Sum of digits are : ",FactorialNum())
	
	number = int(input("please enter Number :"))
	print("Sum of digits are using local variable : ",FactorialNumLocalVariable(number))
	
# code starter 
if __name__ == "__main__":
	main()