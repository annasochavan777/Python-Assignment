#####################################################################
# Write a program which accept one number and display below pattern.
# Input : 5
# Output : * * * * *
#		   * * * *
#		   * * *
#		   * *
#          *
# Author : Annaso Chavan
#####################################################################

# function to print pattern 
def DisplayPattern(no):
	for i in range(no,0,-1): # range(start, stop, step)
		for j in range(i):
			print("*",end=" ")
		print("\n")

def main():
	no = int(input("please enter no :"))
	DisplayPattern(no)
	
		
# code starter 
if __name__ == "__main__":
	main()