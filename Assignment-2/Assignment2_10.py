#####################################################################
# Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37
# Author : Annaso Chavan
#####################################################################

def SumOfDigits(no):
	sum =0
	while no!=0:
		sum += int(no % 10)
		#print(sum)
		no = int(no/10)
		#print(no)
	return sum

def main():
	no = int(input("please enter no :"))
	print("Sum of digits are : ",SumOfDigits(no))
	
		
# code starter 
if __name__ == "__main__":
	main()