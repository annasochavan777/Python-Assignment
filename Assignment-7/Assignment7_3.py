#########################################################################################################
# Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
# Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.
# Author : Annaso Chavan
#########################################################################################################

class Numbers:
	def __init__(self,no):
		self.Value = no
	
	def ChkPrime(self):
		counter = 0
		for i in range(2,self.Value,1): # range(start, stop, step)
			if self.Value % i == 0:
				counter += 1
			if counter > 0:
				break
		return counter == 0
		
	def ChkPerfect(self):
		sum = 0
		for i in range(1,self.Value):
			if self.Value % i == 0:
				sum += i
		return sum == self.Value	
		
	def Factors(self):
		print("factors of {} is ".format(self.Value))
		for i in range(1,self.Value):
			if self.Value % i == 0:
				print(i,end = " ")
		
	def SumFactors(self):
		sum = 0
		for i in range(1,self.Value):
			if self.Value % i == 0:
				sum += i
		return sum
		
def main():
	no = int(input("please enter no :"))
	obj1 = Numbers(no)
	
	isPrime = obj1.ChkPrime()
	if isPrime:
		print("{} is prime number ".format(no))
	else:
		print("{} is not prime number ".format(no))
	
	isPerfect = obj1.ChkPerfect()
	if isPerfect:
		print("{} is Perfect number ".format(no))
	else:
		print("{} is not Perfect number ".format(no))
	
	obj1.Factors()
	
	print("\nsum of factor is ",obj1.SumFactors())
if __name__ == "__main__":
	main()