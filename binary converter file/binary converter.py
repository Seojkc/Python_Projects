from tkinter import *
import math

root=Tk()



e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)




i1 =PhotoImage(file=".\\one.png")

label=Label(root,image=i1)
label.grid(row=6,column=0,columnspan=3)

def click(no):
	p=e.get()
	e.delete(0,END)
	
	global i
	i=e.insert(0,str(p)+str(no))





def con():
	global o
	o=e.get()
	e.delete(0,END)
	b=""
	z=int(o)
	while z>0:
		a=z%2
		b+=str(a)
		z=z//2
   
	e.insert(0,b)










b1=Button(root,text="1",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(1))
b2=Button(root,text="2",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(2))
b3=Button(root,text="3",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(3))

b4=Button(root,text="4",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(4))
b5=Button(root,text="5",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(5))
b6=Button(root,text="6",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(6))

b7=Button(root,text="7",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(7))
b8=Button(root,text="8",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(8))
b9=Button(root,text="9",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(9))

b0=Button(root,text="0",bg="grey",fg="red",padx=40,pady=40,command=lambda:click(0))

bc=Button(root,text="convert",bg="yellow",fg="black",padx=80,pady=40,command=con)


#b1.grid(row=1,column=0)
#b2.grid(row=1,column=1)
#b3.grid(row=1,column=2)

#b4.grid(row=2,column=0)
#b5.grid(row=2,column=1)
#b6.grid(row=2,column=2)

#b7.grid(row=3,column=0)
#b8.grid(row=3,column=1)
#b9.grid(row=3,column=2)

#b0.grid(row=4,column=2)
bc.grid(row=4,column=0,columnspan=2)






root.mainloop()