#####################################################################
# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7
# Author : Annaso Chavan
#####################################################################

def countDigits(no):
	count =0
	while no!=0:
		no = no // 10
		count += 1
	return count
def main():
	no = int(input("please enter no :"))
	print("number of digits are : ",countDigits(no))
	
		
# code starter 
if __name__ == "__main__":
	main()