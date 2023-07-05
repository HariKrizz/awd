from tkinter import *

root = Tk()
root.geometry("200x300")

w = Label(root, text ='GeeksForGeeks', font = "50")

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack( side = RIGHT, fill = Y )

mytext = Text(root, yscrollcommand = scroll_bar.set )

for line in range(1, 26):
	mytext.insert(END, "Geeks " + str(line)+"\n")

mytext.pack()

scroll_bar.config( command = mytext.yview )

root.mainloop()
