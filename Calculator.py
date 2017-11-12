import time
print("Calculator")
var1=int(input("Give the first number:"))
var2=int(input("Give the second number:"))
while True:
	print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit")
	print("Current numbers:",var1,var2,sep=" ")
	choice=int(input("Please select something (1-6):"))
	if choice==1:
		print("The result is:",var1+var2)
	elif choice==2:
		print("The result is:",var1-var2)
	elif choice==3:
		print("The result is:",var1*var2)
	elif choice==4:
		print("The result is:",var1/var2)
	elif choice==5:
		var1=int(input("Give the first number:"))
		var2=int(input("Give the second number:"))
	elif choice==6:
		print("Thank you!!")
		time.sleep(1)
		break
	else:
		print("Selection was not correct.")