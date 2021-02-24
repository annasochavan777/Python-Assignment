##################################################################################################
# Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 32 (13 + 5 + 7 +2 + 5)
# Author : Annaso Chavan
###################################################################################################

from MarvellousNum import *
import functools 

# function to return frequency of that number from List
def ListPrime(arr):
	return list(filter(ChkPrime,arr))

def main():
	arr = []
	number = int(input("Number of elements :"))
	for i in range(number):
		no = int(input("enter {} element :".format(i+1)))
		arr.append(no)
	
	print("Enter Data :",arr)
	
	prime_arr = ListPrime(arr) # call ListPrime function
	
	sum = functools.reduce(Add,prime_arr)
	
	print("Sum of Prime number is :",sum) # print result 
	
# code starter 
if __name__ == "__main__":
	main()