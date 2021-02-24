#########################################################################################################
# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000
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
	
	filter_arr = list(filter(lambda no : (no >= 70 and no <= 90),arr)) # filter the array
	
	print("List after filter = ",filter_arr)

	map_arr = list(map(lambda no : no + 10,filter_arr)) # map the array	
	
	print("List after map = ",map_arr)
	
	product = functools.reduce(lambda a,b : a * b,map_arr) 
	
	print("Output of reduce = ",product)
	
# code starter 
if __name__ == "__main__":
	main()