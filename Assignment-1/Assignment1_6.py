##################################################################################################################
# Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero
# Author : Annaso Chavan
##################################################################################################################

# function to check number is positive or negative or zero
def CheckNum(number):
	if number == 0:
		print("Zero")
	elif number < 0:
		print("Negative Number")
	else:
		print("Positive Number")

def main():
	num = int(input("please enter number :")) # take input from user
	CheckNum(num) # call CheckNum function

# code starter 
if __name__ == "__main__":
	main()