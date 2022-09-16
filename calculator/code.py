from tkinter import *
root=Tk()
root.iconbitmap(".\\sgdfgdfg.ico")
import math
root.title("calculator")
root.configure(background="white")
e=Entry(root,width=45,borderwidth=10)
e.grid(row=0,column=0,columnspan=3,padx=40,pady=20)


root.wm_attributes("-alpha",0.9)

def click(number):
	p=e.get()
	e.delete(0,END)
	
	global i
	i=e.insert(0,str(p)+str(number))


def addo():
	
	global o
	o=e.get()
	e.delete(0,END)
	
	global n
	global math
	math=10
	n=int(o)
	e.delete(0,END)
	


def subo():

	global q
	q=e.get()
	e.delete(0,END)
	m=int(q)
	global w
	global math
	w=0
	w=int(w)+m
	e.delete(0,END)
	math=11


def cro():

	global r
	r=e.get()
	e.delete(0,END)
	m=int(r)
	global t
	global math
	t=0
	t=int(t)+m
	e.delete(0,END)
	math=12


def dio():

	global u
	u=e.get()
	e.delete(0,END)
	m=int(u)
	global h
	global math
	h=0
	h=int(h)+m
	e.delete(0,END)
	math=13



def equalo():
	x=e.get()	
	e.delete(0,END)
	
	if math==10:
		e.insert(0,n+int(x))
	elif math==11:
		e.insert(0,w-int(x))
	elif math==12:
		e.insert(0,t*int(x))
	elif math==13:
		e.insert(0,h/int(x))
	else:
		e.insert(0,"error")

def clear():
	e.delete(0,END)


iclr =PhotoImage(file=".\\clr.png")
i1 =PhotoImage(file=".\\1.png")
i2 =PhotoImage(file=".\\2.png")
i3 =PhotoImage(file=".\\3.png")
i4 =PhotoImage(file=".\\4.png")
i5 =PhotoImage(file=".\\5.png")
i6 =PhotoImage(file=".\\6.png")
i7 =PhotoImage(file=".\\7.png")
i8 =PhotoImage(file=".\\8.png")
i9 =PhotoImage(file=".\\9.png")
i0 =PhotoImage(file=".\\0.png")
isub =PhotoImage(file=".\\minus.png")
iadd =PhotoImage(file=".\\plus.png")
icr =PhotoImage(file=".\\multi.png")
idi =PhotoImage(file=".\\divi.png")
ieq =PhotoImage(file=".\\eqi.png")



b1=Button(root,image=i1,border=0,padx=40,pady=40,command=lambda:click(1))
b2=Button(root,image=i2,border=0,padx=40,pady=40,command=lambda:click(2))
b3=Button(root,image=i3,border=0,padx=40,pady=40,command=lambda:click(3))
b4=Button(root,image=i4,border=0,padx=40,pady=40,command=lambda:click(4))
b5=Button(root,image=i5,border=0,padx=40,pady=40,command=lambda:click(5))
b6=Button(root,image=i6,border=0,padx=40,pady=40,command=lambda:click(6))
b7=Button(root,image=i7,border=0,padx=40,pady=40,command=lambda:click(7))
b8=Button(root,image=i8,border=0,padx=40,pady=40,command=lambda:click(8))
b9=Button(root,image=i9,border=0,padx=40,pady=40,command=lambda:click(9))
b0=Button(root,image=i0,border=0,padx=40,pady=40,command=lambda:click(0))
badd=Button(root,image=iadd,border=0,padx=20,pady=20,command=addo)
bsub=Button(root,image=isub,border=0,padx=20,pady=20,command=subo)
bcr=Button(root,image=icr,border=0,padx=20,pady=20,command=cro)
bdi=Button(root,image=idi,border=0,padx=20,pady=20,command=dio)
beq=Button(root,image=ieq,border=0,padx=20,pady=20,command=equalo)
bclr=Button(root,image=iclr,border=0,padx=20,pady=20,command=clear)


b1.grid(row=3,column=0,)
b2.grid(row=3,column=1,)
b3.grid(row=3,column=2,)

b4.grid(row=2,column=0,)
b5.grid(row=2,column=1,)
b6.grid(row=2,column=2,)

b7.grid(row=1,column=0,)
b8.grid(row=1,column=1,)
b9.grid(row=1,column=2,)

b0.grid(row=4,column=0)
badd.grid(row=5,column=1)
bsub.grid(row=5,column=0)
bcr.grid(row=5,column=2)
bdi.grid(row=4,column=1)




beq.grid(row=4,column=2)
bclr.grid(row=6,columnspan=3)






root.mainloop()

