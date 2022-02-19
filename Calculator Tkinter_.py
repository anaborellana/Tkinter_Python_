from tkinter import ttk
from tkinter import *
from tkinter import colorchooser
import tkinter
from numpy import imag, size
import qrcode
from PIL import ImageTk,Image  


root = Tk()
root.title("QR Code Generator")
myframe = Frame(root)
myframe.pack()

textQRCode = StringVar()
colorFCode = ((),"#00000")
colorBGCode = ((),"#00000")
listVersion = [x for x in range(1,41)]
listSize = [x for x in range(1,41)]

print(listVersion)

''' ----------------------------------- TEXT VALUE ------------------------------------------ '''
title_text = Label(myframe, text = "Text value")
title_text.config(font=10, relief="flat", activeforeground="gray")
title_text.grid(row=0, column=0, pady=7, padx=7, sticky='e')

text_intro = Entry(myframe, textvariable=textQRCode)
text_intro.grid(row=0, column=1, padx=7, columnspan=2, sticky='w')
text_intro.config(justify="center", font=(8))

''' ----------------------------------- VERSION ------------------------------------------ '''
title_version = Label(myframe, text = "Version")
title_version.config(font=(10), relief="flat", activeforeground="gray")
title_version.grid(row=1, column=0, pady=7, padx=7, sticky='e')

combo_version = ttk.Combobox(myframe, values = listVersion)
combo_version.grid(row=1, column=1, padx=7, columnspan=2, sticky='w')
combo_version.current(0)

''' ----------------------------------- SIZE ------------------------------------------ '''
title_size = Label(myframe, text = "Size")
title_size.config(font=(10), relief="flat", activeforeground="gray")
title_size.grid(row=2, column=0, pady=7, padx=7, sticky='e')

combo_size = ttk.Combobox(myframe, values = listSize)
combo_size.grid(row=2, column=1, padx=7, columnspan=2, sticky='w')
combo_size.current(0)

def choose_fcolor():
    global colorFCode
    colorFCode = colorchooser.askcolor(title ="Choose Foreground color")
    label2.config(bg=colorFCode[1])

def choose_bgcolor():
    global colorBGCode
    colorBGCode = colorchooser.askcolor(title ="Choose Background color")
    label1.config(bg=colorBGCode[1])

fcolorButton = Button(myframe, text = "ForeColor", command = choose_fcolor)
fcolorButton.config(font=(10), relief="raised", activeforeground="gray")
fcolorButton.grid(row=3, column=0, columnspan=3, pady=7, padx=7,)

bgcolorButton = Button(myframe, text = "BackgroundColor", command = choose_bgcolor)
bgcolorButton.config(font=(10), relief="raised", activeforeground="gray")
bgcolorButton.grid(row=4, column=0, columnspan=3, pady=7, padx=7)

label1 = Label(myframe)
label1.config(font=(10), relief="flat", activeforeground="gray", bg="white", width = 6, height= 3)
label1.grid(row=5, column=0, columnspan=3, pady=7, padx=7,)

label2 = Label(myframe)
label2.config(font=(10), relief="flat", activeforeground="gray", bg="white", width = 4, height= 2)
label2.grid(row=5, column=0, columnspan=3, pady=7, padx=7)

button9 = Button(myframe,text="Generate", width=9, height=1, command=lambda:generateQRCode())
button9.config(font=(10), relief="raised", activeforeground="gray")
button9.grid(row=6, column=0, columnspan = 3, pady=7, padx=7)

def generateQRCode():
    if textQRCode.get() =="" or textQRCode.get() == "ERROR - You must insert a text to convert to QR Code":
        textQRCode.set("ERROR - You must insert a text to convert to QR Code")
    else:
        try:
            code_1 = qrcode.QRCode(version=combo_version.get(), error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=combo_size.get(), border=2)
            code_1.add_data(textQRCode.get())
            code_1.make()
            img = code_1.make_image(fill_color=colorFCode[1], back_color=colorBGCode[1])
            img.save('qrcode_test1.png')        
        except:
            textQRCode.set("")
    
root.mainloop()
