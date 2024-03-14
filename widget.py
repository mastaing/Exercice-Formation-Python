import tkinter

app = tkinter.Tk()


mainframe = tkinter.Frame(app,)
mainframe.pack()

radio_widget = tkinter.Radiobutton(mainframe , text = "Homme", value = 1)
radio_widget2 = tkinter.Radiobutton(mainframe, text = "Femme", value = 0)

label_mainframe = tkinter.Label(mainframe, text ="Genre")
label_mainframe.pack()

secondframe = tkinter.Frame(app,)
secondframe.pack()

label_secondframe = tkinter.Label(secondframe, text ="age")
label_secondframe.pack()

scale_age = tkinter.Spinbox(secondframe, from_ = 1, to = 100)
scale_age.pack()

radio_widget.pack()
radio_widget2.pack()

app.mainloop()