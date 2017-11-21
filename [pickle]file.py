import pickle
import time

try:
	fname="notebook.dat"
	fh=open(fname,"rb")
except IOError:
	fh=open(fname,"ab")
	print("No default notebook was found, created one.")

content=[]	
while True:
	print("(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit")
	choice=int(input("\nPlease select one:"))
	if choice==1:
		for i in content:
			print(i)
		continue
	elif choice==2:
		txt=input("Write a new note:")
		txt=txt+":::"+time.strftime("%X %x")
		content.append(txt)
		continue
	elif choice==3:
		print("The list has",len(content),"notes.")
		ch=int(input("Which of them will be changed?:"))
		if ch < len(content):
			print(content[ch])
			content.pop(ch)
			new=input("Give the new note:")
			new=new+":::"+time.strftime("%X %x")
			content.insert(ch,new)
		else:
		    print("Incorrect selection")
		continue
	elif choice==4:
		print("The list has",len(content),"notes.")
		dlt=int(input("Which of them will be deleted?:"))
		if dlt < len(content):
			print("Deleted note",content[dlt])
			content.pop(dlt)
		else:
			print("Deleted note",content[dlt-1])
			content.pop(dlt-1)
		continue
	elif choice==5:
		pickle.dump(content,fh)
		fh.close()
		print("Notebook shutting down, thank you.")
		break
	else:
		print("Incorrect selection.")
		continue		