from tkinter import *

root = Tk()
root.title("TicTacToe")

bclick = True
flag = 0


def buttonclick(button):
    global bclick, flag
    if bclick == True and button['text'] == '':
        button['text'] = 'X'
        bclick = False
        flag = flag + 1
    elif bclick == False and button['text'] == '':
        button['text'] = 'O'
        bclick = True
        flag = flag + 1


def disableall():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


label1 = Label(root, text='Player 1 :', font='Times 20 bold',
               fg='black', height=1, width=8)
label1.grid(row=1, column=0)

label2 = Label(root, text='Player 2 :', font='Times 20 bold',
               fg='black', height=1, width=8)
label2.grid(row=2, column=0)

PlayerA = StringVar()
PlayerB = StringVar()

Player1 = StringVar()
Player2 = StringVar()

Player1_name = Entry(root, textvariable=Player1, bd=5)
Player1_name.grid(row=1, column=1)

Player2_name = Entry(root, textvariable=Player2, bd=5)
Player2_name.grid(row=2, column=1)

button1 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button1))
button1.grid(row=3, column=0)
button2 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button2))
button2.grid(row=3, column=1)
button3 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button3))
button3.grid(row=3, column=2)
button4 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button4))
button4.grid(row=4, column=0)
button5 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button5))
button5.grid(row=4, column=1)
button6 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button6))
button6.grid(row=4, column=2)
button7 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button7))
button7.grid(row=5, column=0)
button8 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button8))
button8.grid(row=5, column=1)
button9 = Button(root, text='', font='Times 20 bold', bg='grey',
                 fg='black', height=4, width=8, command=lambda: buttonclick(button9))
button9.grid(row=5, column=2)


root.mainloop()
