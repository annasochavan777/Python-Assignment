################################################################################################################
# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56
# Author : Annaso Chavan
################################################################################################################

# function to Return Maximum number from List
def FindMaxNum(arr):
	max = 0
	for i in range(len(arr)):
		if max <= arr[i]:
			max = arr[i]
	return max

def main():
	arr = []
	number = int(input("Number of elements :"))
	for i in range(number):
		no = int(input("enter {} element :".format(i+1)))
		arr.append(no)

	max_num = FindMaxNum(arr) # call FindMaxNum function
	print("Maximum number is :",max_num) # print result 
	
# code starter 
if __name__ == "__main__":
	main()