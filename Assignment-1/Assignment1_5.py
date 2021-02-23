#####################################################################################
# Write a program which display 10 to 1 on screen.
# Output : 10 9 8 7 6 5 4 3 2 1
# Author : Annaso Chavan
#####################################################################################

# print the number in reverse order 
def main():
	for i in range(10,0,-1): # range(start, stop, step)
		print(i, end =" ") 
	
# code starter 
if __name__ == "__main__":
	main()