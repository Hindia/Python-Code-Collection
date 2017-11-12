#easy python code for understanding read/write/append file
import time#for using sleep() function
while True:
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
	choice=int(input("Please select one:"))
	if choice==1:
		handler=open("notebook.txt","r")
		content=handler.read()
		print(content)
		handler.close()
		continue
	elif choice==2:
		handler=open("notebook.txt","a")
		text=input("write a new note:")
		handler.write(text)
		handler.close()
		continue
	elif choice==3:
		handler=open("notebook.txt","w")
		handler.close()
		print("Notes deleted.")
		continue
	elif choice==4:
		print("Notebook shutting down, thank you.")
		time.sleep(1)
		break
	else:
		print("Incorrect selection")
		continue