from tkinter import*
import winsound

win = Tk()
win.title("Bruh-Calc")

icon = PhotoImage(file = "4c5.png")
win.iconphoto(False, icon)

Terminal = Entry(win, fg="green", font="courier 20", width=20, justify="center")
global num1
global num2
global prod
global op
op = None
prod = 0
num1 = 0
num2 = 0


def Terminal_fill(num):
    Terminal.insert(END, num)
    print(Terminal.get())

def Operator(sign):
    global op
    global num1
    op = sign
    num1 = int(Terminal.get())
    Terminal.delete(0, END)

def equal():
    global num2
    global prod
    global num1
    global op
    winsound.Beep(2000,500)
    num2 = int(Terminal.get())
    Terminal.delete(0, END)
    if op == "+" :
        prod = num1 + num2
    elif op == "-" :
        prod= num1 - num2
    elif op=="X" :
        prod = num1*num2
    elif op=="/":
        prod= num1/num2
    elif op == None:
        prod = num2
    Terminal.insert(0,prod)




def clear():
    global op
    op=None
    Terminal.delete(0,END)


B1 = Button(win, text="1", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(1))
B2 = Button(win, text="2", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(2))
B3 = Button(win, text="3", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(3))
B4 = Button(win, text="4", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(4))
B5 = Button(win, text="5", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(5))
B6 = Button(win, text="6", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(6))
B7 = Button(win, text="7", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(7))
B8 = Button(win, text="8", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(8))
B9 = Button(win, text="9", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(9))
B0 = Button(win, text="0", font="courier", fg="green", width=7, height=3, command=lambda: Terminal_fill(0))

Clear = Button(win, text="Clear", font="courier", fg="green", width=7, height=7, command = lambda: clear())
Equals = Button(win, text="=", font="courier", fg="green", width=7, height=7, command=lambda: equal())
Plus = Button(win, text="+", font="courier", fg="green", width=7, height=3, command=lambda: Operator("+"))
minus = Button(win, text="-", font="courier", fg="green", width=7, height=3, command=lambda: Operator("-"))
multi = Button(win, text="X", font="courier", fg="green", width=7, height=3, command=lambda: Operator("X"))
divide = Button(win, text="/", font="courier", fg="green", width=7, height=3, command=lambda: Operator("/"))

Terminal.grid(row=0, column=0, columnspan=3)

B1.grid(row=1, column=0)
B2.grid(row=1, column=1)
B3.grid(row=1, column=2)

B4.grid(row=2, column=0)
B5.grid(row=2, column=1)
B6.grid(row=2, column=2)

B7.grid(row=3, column=0)
B8.grid(row=3, column=1)
B9.grid(row=3, column=2)

B0.grid(row=4, column=0)
Clear.grid(row=5, column=1, rowspan=2)
Equals.grid(row=5, column=2, rowspan=2)

Plus.grid(row=5, column=0)

minus.grid(row=6, column=0)
multi.grid(row=4, column=1)
divide.grid(row=4, column=2)

win.mainloop()