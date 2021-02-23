#####################################################################
# Write a program which accept one number and display below pattern.
# Input : 5
# Output : 1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
#          1 2 3 4 5
# Author : Annaso Chavan
#####################################################################

# function to print pattern 
def DisplayPattern(no):
	for i in range(1,no+1,1): # range(start, stop, step)
		for j in range(1,no+1,1):
			print(j,end=" ")
		print("\n")

def main():
	no = int(input("please enter no :"))
	DisplayPattern(no)
	
		
# code starter 
if __name__ == "__main__":
	main()