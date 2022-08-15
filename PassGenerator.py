
from tkinter import *
import random
import string

#My Window
mywin=Tk()
mywin.title("Password Generator")
mywin.geometry("500x400")

title=StringVar()
choice=IntVar()
label=Label(mywin,textvariable=title).pack()
title.set("Select the strength of password")

def selection():
    global selection
    selection=choice.get()

#Slecting password strength
R1=Radiobutton(mywin, text="Poor",variable=choice,value=1,command =selection).pack(anchor=CENTER)
R2=Radiobutton(mywin, text="Average",variable=choice,value=2,command =selection).pack(anchor=CENTER)
R3=Radiobutton(mywin, text="Strong",variable=choice,value=3,command =selection).pack(anchor=CENTER)
Label.choice=Label(mywin).pack()



# Selecting password length
lenlabel=StringVar()
val= IntVar()
lenlabel.set("Password Length")
lentitle=Label(mywin,textvariable=lenlabel).pack()

#Length selection
spinlen= Spinbox(mywin, from_=4, to_=24, textvariable=val, width=15).pack()

# password print
def callback():
    lsum.config(text=passgen())

#clickable button
passgenButton=Button(mywin,text="Generate Password",bd=5,height=2,command=callback, bg='lightblue').pack()
lsum=Label(mywin, text="")
lsum .pack(side=BOTTOM)
Password=str(callback)

#Fuction
Poor=string.ascii_uppercase + string.ascii_lowercase
Average=string.ascii_uppercase + string.ascii_lowercase + string.digits
Advance=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

# Generate random password of specified length
def passgen():

    if choice.get()== 1:
        return "".join(random.sample(Poor,val.get()))
    elif choice.get()==2:
        return " ".join(random.sample(Average,val.get()))
    elif choice.get()==3:
        return " ".join(random.sample(Advance,val.get()))

mywin.mainloop()

