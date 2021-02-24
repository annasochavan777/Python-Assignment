################################################################################################################
# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5
# Author : Annaso Chavan
################################################################################################################

# function to Return Minimum number from List
def FindMinNum(arr):
	min = 0
	for i in range(len(arr)):
		if min == 0:
			min = arr[i]
		if min >= arr[i]:
			min = arr[i]
	return min

def main():
	arr = []
	number = int(input("Number of elements :"))
	for i in range(number):
		no = int(input("enter {} element :".format(i+1)))
		arr.append(no)

	min_num = FindMinNum(arr) # call FindMinNum function
	print("Minimum number is :",min_num) # print result 
	
# code starter 
if __name__ == "__main__":
	main()