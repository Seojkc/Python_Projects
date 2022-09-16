from tkinter import *
import tkinter.messagebox


root=Tk()
#root.iconbitmap("D:\\seo\\tic tac toe\\favicon.ico")
root.title("Tic Tac Toe")
root.configure(bg="black")





i1=PhotoImage(file=".\\clr.png")
i2=PhotoImage(file=".\\download.png")
i3=PhotoImage(file=".\\uncxnamed.png")
i5=PhotoImage(file=".\\clr.png")
i7=PhotoImage(file=".\\Untidsvfssssssssssssssssssssssstled.png")



def koi():

    tk = Toplevel()

    tk.title("Tic Tac Toe")
   # tk.iconbitmap("uncxnamed.png")

    global bclick, flag, player2_name, player1_name, playerb, pa
    pa = StringVar()
    playerb = StringVar()
    p1 = StringVar()
    p2 = StringVar()



    bclick = True
    flag = 0

    def disableButton():
        button1.configure(text=" ")
        button2.configure(text=" ")
        button3.configure(text=" ")
        button4.configure(text=" ")
        button5.configure(text=" ")
        button6.configure(text=" ")
        button7.configure(text=" ")
        button8.configure(text=" ")
        button9.configure(text=" ")



    def btnClick(buttons):
        global bclick, flag, player2_name, player1_name, playerb, pa
        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "X"
            bclick = False

            checkForWin()  
            flag += 1


        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "O"
            bclick = True
            checkForWin()
            flag += 1
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

    iclear=PhotoImage(file=".\\clr.png")

    def booclick():
        global flag
        player2_name.delete(0,END)
        player1_name.delete(0,END)
        disableButton()
        flag = 0

    def checkForWin():
        global flag

        if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' ):
           
            disableButton()
            lo = "  *  "
            player1_name.insert(0,lo)
  
            flag=0
                   

        elif(flag == 8):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

        elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
              button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
              button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
              button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
              button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
              button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
              button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
              button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
            disableButton()
            kj=IntVar()
            kj=1
            po = "  *  "
            player2_name.insert(0,po)
           
            
            flag=0
            #tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


    #buttons = StringVar()

    player1_name = Entry(tk, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=8)
    player2_name = Entry(tk, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=8)








    label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=1, column=0)


    label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
    label.grid(row=2, column=0)

    button1 = Button(tk, text=" ", font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=' ',font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(tk, text=' ', font='Times 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)


    buttoncl=Button(tk,image=i5,padx=120,pady=40,command=booclick)
    buttoncl.grid(row=6,column=0,columnspan=2)

    buttonx=Button(tk,image=i7,padx=20,pady=40,command=tk.destroy)
    buttonx.grid(row=6,column=2,columnspan=1)

l12=Label(root,image=i3,borderwidth=0).grid(row=0,column=0)
l13=Button(root,image=i2,borderwidth=0,command=koi).grid(row=2,column=0)


mainloop()
