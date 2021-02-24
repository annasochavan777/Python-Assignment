#########################################################################################################
# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62
# Author : Annaso Chavan
#########################################################################################################

import functools

# function to check whether number is prime or not 
def IsPrimeNumber(no):
	counter = 0
	for i in range(2,no,1): # range(start, stop, step)
		if no % i == 0:
			counter += 1
		if counter > 0: # if counter incremented by 1 means number is not a prime number so no need to triverse loop further so break the loop early 
			break
	return counter == 0

# function to Return Maximum number from List
def FindMaxNum(no1,no2):
		if no1 <= no2:
			return no2
		else:
			return no1
	
def main():
	arr = []
	number = int(input("Number of elements :"))
	for i in range(number):
		no = int(input("enter {} element :".format(i+1)))
		arr.append(no)
	
	print("Input List = ",arr)
	
	filter_arr = list(filter(IsPrimeNumber,arr)) # filter the array
	
	print("List after filter = ",filter_arr)

	map_arr = list(map(lambda no : no * 2,filter_arr)) # map the array	
	
	print("List after map = ",map_arr)
	
	max = functools.reduce(FindMaxNum,map_arr) 
	
	print("Output of reduce = ",max)
	
# code starter 
if __name__ == "__main__":
	main()