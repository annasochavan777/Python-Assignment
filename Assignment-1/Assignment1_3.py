#####################################################################################################
# Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5 Output : 16
# Author : Annaso Chavan
#####################################################################################################

# function to Add two number
def Add(val1,val2):
	return val1 + val2
	
def main():
	try:
		first = int(input("please enter first no :"))
		second= int(input("please enter second no :"))
	except:
		print("An exception occurred...Only integers are allowed")
	
	ans = Add(first,second) # call Add function
	
	print("addition is :",ans) # print result 
	
# code starter 
if __name__ == "__main__":
	main()