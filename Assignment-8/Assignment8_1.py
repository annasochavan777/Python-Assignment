#########################################################################################################
# Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd numbers. 
# Author : Annaso Chavan
#########################################################################################################

import threading

def Even():
	print("Even numbers are ")
	count = 1
	i = 1
	while count != 10:
		if i % 2 == 0:
			print(i, end=" ")
			count += 1
		i += 1

def Odd():
	print("\nOdd numbers are ")
	count = 1
	i = 1
	while count != 10:
		if i % 2 == 1:
			print(i, end=" ")
			count += 1
		i += 1
	
def main():
	t1 = threading.Thread(target = Even)
	t2 = threading.Thread(target = Odd)
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
if __name__ == "__main__":
	main()

