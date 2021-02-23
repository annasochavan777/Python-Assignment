###########################################################################################
# Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20
# Author : Annaso Chavan
###########################################################################################

# function to display first 10 even numbers
def DisplayEvenNo():
	count = 0
	no = 1
	while count != 10:
		if no % 2 == 0:
			print(no,end=" ")
			count += 1
		no +=1

def main():
	DisplayEvenNo() # call Display function
	
# code starter 
if __name__ == "__main__":
	main()