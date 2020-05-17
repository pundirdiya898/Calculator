import tkinter
from tkinter import *
#simple calculator in python using Tkinter
# Click function for appending numbers
def Click(numbers):
    global operator
    operator=operator+str(numbers)
    text.set(operator)
# to clear the screen
def btnClear():
    global operator
    operator=""
    text.set("")
# to get result
def btnEquals():
    global operator
    sumup=str(eval(operator))
    text.set(sumup)
    operator=""
# creating window for calculator   
win = Tk()
win.title("Calculator")
operator=""
text=StringVar()

textDisplay=Entry(win,font=("Calliber",20,"bold"),textvariable=text,bd=30,bg="#566666").grid(columnspan=4)
#Entry.grid(columnspan=4)

button7=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="7",command=lambda:Click(7))
button7.grid(row=1,column=0)

button8=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="8",command=lambda:Click(8))
button8.grid(row=1,column=1)

button9=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="9",command=lambda:Click(9))
button9.grid(row=1,column=2)

buttonAdd=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="+",command=lambda:Click("+"))
buttonAdd.grid(row=1,column=3)



button4=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="4",command=lambda:Click(4))
button4.grid(row=2,column=0)

button5=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="5",command=lambda:Click(5))
button5.grid(row=2,column=1)

button6=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="6",command=lambda:Click(6))
button6.grid(row=2,column=2)

buttonSub=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="-",command=lambda:Click("-"))
buttonSub.grid(row=2,column=3)



button1=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="1",command=lambda:Click(1))
button1.grid(row=3,column=0)

button2=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="2",command=lambda:Click(2))
button2.grid(row=3,column=1)

button3=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="3",command=lambda:Click(3))
button3.grid(row=3,column=2)

buttonMul=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="*",command=lambda:Click("*"))
buttonMul.grid(row=3,column=3)


button0=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="0",command=lambda:Click(0))
button0.grid(row=4,column=0)

buttonClr=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="C",command=btnClear)
buttonClr.grid(row=4,column=1)

buttonEqu=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="=",command=btnEquals)
buttonEqu.grid(row=4,column=2)

buttonDiv=Button(win,padx=16,pady=16,bd=8,fg="black",font=('Calliber',20,'bold'),text="/",command=lambda:Click("/"))
buttonDiv.grid(row=4,column=3)


win.mainloop()
