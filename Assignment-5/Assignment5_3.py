#########################################################################################################
# Write a recursive program which display below pattern.
# Input : 5
# Output : 5 4 3 2 1
# Author : Annaso Chavan
#########################################################################################################

def Display(no):
	if no != 0:
		print(no,end =" ")
		no -= 1
		Display(no)

def main():
	number = int(input("please enter Number :"))
	Display(number)
	
# code starter 
if __name__ == "__main__":
	main()