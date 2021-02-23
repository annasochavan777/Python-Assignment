###########################################################################################
# Write a program which accept number from user and print that number of "*" on screen.
# Input : 5 Output : * * * * *
# Author : Annaso Chavan
###########################################################################################

def Display(num):
	for i in range(num):
		print("*",end=" ") 

def main():
	num = int(input("please enter number how many time you want to print * ? :")) # take input from user
	Display(num) # call Display function
	
# code starter 
if __name__ == "__main__":
	main()