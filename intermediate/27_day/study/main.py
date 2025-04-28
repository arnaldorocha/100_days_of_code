# import turtle

# turtle.Turtle()

from tkinter import *
# from tkinter import Tk

window = Tk()
window.title("Simple GUI")
window.minsize(width=500,height= 300)

#Label
my_label = Label(text="I am Label", font = ("Arial", 24, "bold"))
my_label.pack(side = "left")


my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
print(input.get())


mainloop()