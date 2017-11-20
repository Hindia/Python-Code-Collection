import math
def ask():
	while True:
		try:
			number = int(input("Give a number: "))
			return number
			break
		except Exception:
			print("This input is invalid.")

def main():
    print("Calculator")
    number1=ask()
    number2=ask()
    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
        print("Current numbers:",number1,number2)
        try:
            selection = int(input("Please select something (1-6): "))
            if selection == 1:
        	    print("The result is:", number1+number2)
            elif selection == 2:
        	    print("The result is:", number1-number2)
            elif selection == 3:
        	    print("The result is:", number1*number2)
            elif selection == 4:
        	    print("The result is:", number1/number2)
            elif selection == 5:
                print("The result is:", math.sin(number1/number2))
            elif selection == 6:
                print("The result is:", math.cos(number1/number2))
            elif selection == 7:
        	    number1 = int(input("Give the first number: "))
        	    number2 = int(input("Give the second number: "))
            elif selection == 8:
        	    print("Thank you!")
        	    break
        except Exception:
            print("Selection was not correct.")
			
if __name__=="__main__":
	main()

	