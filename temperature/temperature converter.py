

 #temperature converter
from tkinter import *


root=Tk()

root.configure(bg="white")

def f():
	try:
		q=e.get()
		e.delete(0,END)
		u=int(q)
		o=((9/5)*u)+32
		e1.delete(0,END)
		e1.insert(0,"   `F") 
		e1.insert(0,o)	
	except:
		e1.delete(0,END)
		e.delete(0,END)
		e.insert(0,"type anything")
		e1.insert(0,"പോടാ പട്ടി")

def c():
	try:

		q=e.get()
		e.delete(0,END)
		u=int(q)
		o=(u-32)*(5/9)
		e1.delete(0,END)
		e1.insert(0,"  `C")
		e1.insert(0,o)
	except:
		e.delete(0,END)
		e1.delete(0,END)
		e.insert(0,"type anything")
		e1.insert(0,"പോടാ പട്ടി")



i1 =PhotoImage(file=".\\Untitled.png")

lo=Label(root,image=i1)
lo.grid(row=0,column=0)

e=Entry(root,width=65,borderwidth=5)
e.grid(row=2,column=1,padx=35,pady=10)

l=Label(root,fg="black",text="Enter the degree :",font="times 20")
l.grid(row=2,column=0)

ql=Label(root,text=" into  ",font="times 16")
ql.grid(row=3,column=0)

b=Button(root,bg="green",text="celsius",padx=20,pady=10,borderwidth=10,command=c)
b.grid(row=3,column=1)

ql2=Label(root,text="   ")
ql2.grid(row=3,column=2)

b1=Button(root,bg="green",text="farenheit",padx=20,pady=10,borderwidth=10,command=f)
b1.grid(row=3,column=3)

ql24=Label(root,text="   ")
ql24.grid(row=3,column=4)

ql3=Label(root,text=" Result  ",font="times 20")
ql3.grid(row=4,column=0)

e1=Entry(root,width=85,borderwidth=5)
e1.grid(row=4,column=1,padx=55,pady=10)


root.mainloop()                                               