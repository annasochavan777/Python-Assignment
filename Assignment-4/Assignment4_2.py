#########################################################################################################
# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18
# Author : Annaso Chavan
#########################################################################################################

multi = lambda no1,no2 : no1 * no2

def main():
	no1 = int(input("please enter first number :"))
	no2 = int(input("please enter second number :"))
	
	print("Multiplication of {} & {} is : {}".format(no1,no2,multi(no1,no2))) # print result 
	
# code starter 
if __name__ == "__main__":
	main()