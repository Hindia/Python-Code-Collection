import time
try:
	fname="notebook.txt"
	handler=open(fname,"r")
except IOError:
	handler=open(fname,"a")
	print("No default notebook was found, created one.")

while True:
    print("Now using file",fname,"\n(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit\n")
    choice=int(input("Please select one:"))
    if choice==1:
        handler=open(fname,"r")
        content=handler.read()
        print(content)
        handler.close()
        continue
    elif choice==2:
        handler=open(fname,"a")
        text=input("write a new note:")
        date=time.strftime("%X %x")
        text=text+":::written on/at "+date+"\n"
        handler.write(text)
        handler.close()
        continue
    elif choice==3:
        handler=open(fname,"w")
        handler.close()
        print("Notes deleted.")
        continue
    elif choice==4:
        fname=input("Give the name of the new file:")
        try:
            handler.close()
            handler1=open(fname,"r")
        except IOError:
            handler1=open(fname,"a")
            print("No notebook with that name detected, created one.")
            continue		
    elif choice==5:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")
        continue