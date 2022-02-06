from tkinter import *

root=Tk()
root.title("Calculator")
myFrame = Frame(root)
myFrame.pack()

'''------------------------------- Global variables ----------------------------------'''

vOperation = StringVar()
screenOperation = StringVar()
screenError = StringVar()

screenNumber = Entry(myFrame, textvariable=screenOperation)
screenNumber.grid(row=1, column=0, padx= 10, pady = 10, columnspan=4)
screenNumber.config(justify="center", font=(8))

screenTotalHistory =Text(myFrame, width=16, height=5, padx=80, pady=10)
screenTotalHistory.grid(row=9, column=0, columnspan=4)

scrollV= Scrollbar(myFrame,command=screenTotalHistory.yview)
scrollV.grid(row=9, column=4,sticky="ns")
screenTotalHistory.config(yscrollcommand=scrollV.set)

screenNumberError = Entry(myFrame, textvariable=screenError)
screenNumberError.grid(row=8, column=0, padx= 10, pady = 10, columnspan=4)
screenNumberError.config(justify="center", font=(8))


def buttonScreen(operation):
    screenError.set("")
    try:
        vOperation.set(vOperation.get() + operation)
        print(vOperation.get())
        screenOperation.set(vOperation.get())
    except:
        screenError.set("ERROR")
    
def result():
    try:
        print(eval(vOperation.get()))
        screenOperation.set(eval(vOperation.get()))
        screenTotalHistory.insert(END,"{} = {}\n".format(vOperation.get(), eval(vOperation.get())))
        vOperation.set(eval(vOperation.get()))
    except SyntaxError:
        screenError.set("ERROR")

def erase():
    vOperation.set("")
    screenOperation.set("")
    screenError.set("")
        
'''------------------------------- Number buttons ----------------------------------'''

button9 = Button(myFrame,text="9", width=5, height=2, command=lambda:buttonScreen("9"))
button9.config(font=(42), relief="groove", activeforeground="gray")
button9.grid(row=3, column=2, pady= 7)

button8 = Button(myFrame,text="8", width=5, height=2, command=lambda:buttonScreen("8"))
button8.config(font=(42), relief="groove", activeforeground="gray")
button8.grid(row=3, column=1, pady= 7)

button7 = Button(myFrame,text="7", width=5, height=2, command=lambda:buttonScreen("7"))
button7.config(font=(42), relief="groove", activeforeground="gray")
button7.grid(row=3, column=0, pady= 7)

button6 = Button(myFrame,text="6", width=5, height=2, command=lambda:buttonScreen("6"))
button6.grid(row=4, column=2, pady= 7)
button6.config(font=(42), relief="groove", activeforeground="gray")

button5 = Button(myFrame,text="5", width=5, height=2, command=lambda:buttonScreen("5"))
button5.grid(row=4, column=1, pady= 7)
button5.config(font=(42), relief="groove", activeforeground="gray")

button4 = Button(myFrame,text="4", width=5, height=2, command=lambda:buttonScreen("4"))
button4.grid(row=4, column=0, pady= 7)
button4.config(font=(42), relief="groove", activeforeground="gray")

button3 = Button(myFrame,text="3", width=5, height=2, command=lambda:buttonScreen("3"))
button3.grid(row=5, column=2, pady= 7)
button3.config(font=(42), relief="groove", activeforeground="gray")

button2 = Button(myFrame,text="2", width=5, height=2, command=lambda:buttonScreen("2"))
button2.grid(row=5, column=1, pady= 7)
button2.config(font=(42), relief="groove", activeforeground="gray")

button1 = Button(myFrame,text="1", width=5, height=2, command=lambda:buttonScreen("1"))
button1.grid(row=5, column=0, pady= 7)
button1.config(font=(42), relief="groove", activeforeground="gray")

button0 = Button(myFrame,text="0", width=5, height=2, command=lambda:buttonScreen("0"))
button0.grid(row=6, column=0, pady= 7)
button0.config(font=(42), relief="groove", activeforeground="gray")


'''------------------------------- Operation buttons ----------------------------------'''

buttonDiv = Button(myFrame,text="/", width=5, height=2, command=lambda:buttonScreen("/"))
buttonDiv.grid(row=3, column=3, pady= 7)
buttonDiv.config(font=(42), relief="groove", activeforeground="gray")

buttonMult = Button(myFrame,text="x", width=5, height=2, command=lambda:buttonScreen("*"))
buttonMult.grid(row=4, column=3, pady= 7)
buttonMult.config(font=(42), relief="groove", activeforeground="gray")

buttonRest = Button(myFrame,text="-", width=5, height=2, command=lambda:buttonScreen("-"))
buttonRest.grid(row=5, column=3, pady= 7)
buttonRest.config(font=(42), relief="groove", activeforeground="gray")

buttonComma = Button(myFrame,text=",", width=5, height=2, command=lambda:buttonScreen(","))
buttonComma.grid(row=6, column=1, pady= 7)
buttonComma.config(font=(42), relief="groove", activeforeground="gray")

buttonSum = Button(myFrame,text="+", width=5, height=2, command=lambda:buttonScreen("+"))
buttonSum.grid(row=6, column=3, pady= 7)
buttonSum.config(font=(42), relief="groove", activeforeground="gray")


'''------------------------------- esults buttons ----------------------------------'''

buttonEq = Button(myFrame,text="=", width=5, height=2, command=lambda:result())
buttonEq.grid(row=6, column=2, pady= 7)
buttonEq.config(font=(42), relief="groove", activeforeground="gray")

buttonErase = Button(myFrame, text="Erase", width=5, height=2, command=lambda:erase())
buttonErase.grid(row=7, column=0, columnspan=4, pady= 7)
buttonErase.config(font=(42), relief="groove", activeforeground="gray")

root.mainloop()