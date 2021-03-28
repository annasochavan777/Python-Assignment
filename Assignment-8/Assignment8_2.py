#########################################################################################################
# Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as "exit from main".  
# Author : Annaso Chavan
#########################################################################################################

import threading

def EvenFactor(no):
	i = 1
	sum = 0
	while no != i:
		if (no % i == 0) and (i % 2 == 0):
			sum += i
		i += 1
	print("Even Factor sum is ",sum)
	
def OddFactor(no):
	i = 1
	sum = 0
	while no != i:
		if no % i == 1:
			sum += i
		i += 1
	print("Odd Factor sum is ",sum)
	
def main():
	no = int(input("please enter no :"))
	t1 = threading.Thread(target = EvenFactor, args = (no,))
	t2 = threading.Thread(target = OddFactor, args = (no,))	
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
if __name__ == "__main__":
	main()