#####################################################################
# Write a program which accept one number and display below pattern.
# Input : 5
#  Output : * * * * *
#			* * * * *
#			* * * * *
#			* * * * *
#			* * * * *
# Author : Annaso Chavan
#####################################################################

def Display(no):
	for i in range(no):
		for j in range(5):
			print("*",end=" ")
		print("\n")

def main():
	no = int(input("please enter no :"))
	Display(no)

# code starter 
if __name__ == "__main__":
	main()