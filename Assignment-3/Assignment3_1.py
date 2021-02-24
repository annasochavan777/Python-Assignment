###########################################################################################################################
# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130
# Author : Annaso Chavan
###########################################################################################################################

# function to return addition of all elements
def Addition(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i]
	return sum

def main():
	arr = []
	number = int(input("Number of elements :"))
	for i in range(number):
		no = int(input("enter {} element :".format(i+1)))
		arr.append(no)

	add_ans = Addition(arr) # call Addition function
	print("addition is :",add_ans) # print result 
	
# code starter 
if __name__ == "__main__":
	main()