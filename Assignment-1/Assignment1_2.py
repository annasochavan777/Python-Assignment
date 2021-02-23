#########################################################################################################################
# Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number
# Author : Annaso Chavan
#########################################################################################################################

# function to check number is even or odd
def ChkNum(num):
	if num % 2 == 0:
		return True # Even
	else:
		return False # Odd

# code starter 
if __name__ == "__main__":
	try:
		number = int(input("Please enter number :"))
	except:
		print("An exception occurred...Only integers are allowed")
	
	# call the ChkNum() function
	result = ChkNum(number)
	
	if result:
		print("{} is Even number".format(number))
	else:
		print("{} is Odd number".format(number))