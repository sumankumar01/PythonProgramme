import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()


mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x480+200")
label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.grid(row=0, column=0)
canvas.pack(side='left', fill=tkinter.X, expand=True)

button1 = tkinter.Button(mainWindow, text='button1')
button2 = tkinter.Button(mainWindow, text='button2')
button3 = tkinter.Button(mainWindow, text='button3')

button1.pack(side='left', anchor='n')
button2.pack(side='left', anchor='s')
button3.pack(side='left', anchor='e')

mainWindow.mainloop()
