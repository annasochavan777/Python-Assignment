#########################################################################################################
# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204
# Author : Annaso Chavan
#########################################################################################################

import functools

def main():
	arr = []
	number = int(input("Number of elements :"))
	for i in range(number):
		no = int(input("enter {} element :".format(i+1)))
		arr.append(no)
	
	print("Input List = ",arr)
	
	filter_arr = list(filter(lambda no : (no % 2 == 0),arr)) # filter the array
	
	print("List after filter = ",filter_arr)

	map_arr = list(map(lambda no : no ** 2,filter_arr)) # map the array	
	
	print("List after map = ",map_arr)
	
	product = functools.reduce(lambda a,b : a + b,map_arr) 
	
	print("Output of reduce = ",product)
	
# code starter 
if __name__ == "__main__":
	main()