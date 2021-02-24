################################################################################################################
# Write a program which accept N numbers from user and store it into List. Accept one another number from user and 
# return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3
# Author : Annaso Chavan
################################################################################################################

# function to return frequency of that number from List
def CheckFrequencyOfNum(arr,search_element):
	return arr.count(search_element)

def main():
	arr = []
	number = int(input("Number of elements :"))
	for i in range(number):
		no = int(input("enter {} element :".format(i+1)))
		arr.append(no)
	
	number = int(input("Element to search :"))
	
	result = CheckFrequencyOfNum(arr,number) # call CheckFrequencyOfNum function
	print("Output :",result) # print result 
	
# code starter 
if __name__ == "__main__":
	main()