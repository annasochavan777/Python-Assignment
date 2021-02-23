#####################################################################
# Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120
# Author : Annaso Chavan
#####################################################################

# calculate factorial of number 
def FactorialNum(no):
	fact = 0
	for i in range(no,0,-1): # range(start, stop, step)
		if fact == 0:
			fact = i
		else:
			fact = fact * i
	print("Factorial of {} number is : {}".format(no,fact))

def main():
	no = int(input("please enter no :"))
	FactorialNum(no) # call factorial function

# code starter 
if __name__ == "__main__":
	main()