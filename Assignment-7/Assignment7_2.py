#########################################################################################################
# Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.
# Author : Annaso Chavan
#########################################################################################################

class BankAccount:
	ROI = 10.5
	def __init__(self,name,amount):
		self.Name = name
		self.Amount = amount
	
	def Display(self):
		print("Name = ",self.Name)
		print("Amount =",self.Amount)
		
	def Deposit(self):
		amount = int(input("Enter amount that you want to deposit ?"))
		self.Amount = amount
		pass
	
	def Withdraw(self):
		amount = int(input("Enter amount that you want to Withdraw ?"))
		self.Amount -= amount
	
	def CalculateIntrest(self):
		intrest = (self.Amount * BankAccount.ROI) / 100
		self.Amount += intrest
		
def main():
	obj1 = BankAccount("Annaso",0)
	obj1.Deposit()
	obj1.Withdraw()
	obj1.CalculateIntrest()
	obj1.Display()
	
if __name__ == "__main__":
	main()