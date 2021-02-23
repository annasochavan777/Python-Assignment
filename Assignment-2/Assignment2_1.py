###########################################################################################################################
# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for 
# multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.
# Author : Annaso Chavan
###########################################################################################################################

from Arithmetic import *

def main():
	try:
		first = int(input("please enter first no :"))
		second= int(input("please enter second no :"))
	except:
		print("An exception occurred...Only integers are allowed")
	
	add_ans = Add(first,second) # call Add function
	print("addition is :",add_ans) # print result 
	
	sub_ans = Sub(first,second) # call Sub function
	print("Substraction is :",sub_ans) # print result 
	
	div_ans = Div(first,second) # call Div function
	print("Division is :",div_ans) # print result 
	
	multi_ans = Multi(first,second) # call Multi function
	print("Multiplication is :",multi_ans) # print result 
	
# code starter 
if __name__ == "__main__":
	main()