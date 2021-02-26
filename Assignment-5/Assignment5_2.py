#########################################################################################################
# Write a recursive program which display below pattern.
# Input : 5
# Output : 1 2 3 4 5
# Author : Annaso Chavan
#########################################################################################################

i = 0 
def Display(no):
	global i
	if i != no:
		print(i+1,end =" ")
		i += 1
		Display(no)

def main():
	number = int(input("please enter Number :"))
	Display(number)
	
# code starter 
if __name__ == "__main__":
	main()