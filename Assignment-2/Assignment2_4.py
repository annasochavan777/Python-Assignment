#####################################################################
# Write a program which accept one number form user and return addition of its factors.
# Input : 12 Output : 16 (1+2+3+4+6)
# Author : Annaso Chavan
#####################################################################

# function to return addition of its factors 
def Addition(no):
	sum = 0
	for i in range(1,no,1): # range(start, stop, step)
		if no % i == 0:
			sum += i
	return sum

def main():
	no = int(input("please enter no :"))
	print("addition of its factors is :",Addition(no)) # call Addition function

# code starter 
if __name__ == "__main__":
	main()