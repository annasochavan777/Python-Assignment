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
		pass
		
	def ChkPerfect(self):
		pass
		
	def Factors(self):
		pass
		
	def SumFactors(self):
		pass
		
def main():
	no = int(input("please enter no :"))
	
if __name__ == "__main__":
	main()