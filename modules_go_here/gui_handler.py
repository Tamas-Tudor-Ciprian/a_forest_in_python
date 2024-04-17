import tkinter
import os
import customtkinter  # <- import the CustomTkinter module

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("400x120")
root_tk.title("Forest fire simulation")


def random_start(event):
    os.system("start cmd /k python random_fire.py")

def center_start(event):
    os.system("start cmd /k python center_fire.py")



random_start_button = tkinter.Button(
    text="Random",
    width=10,
    height=2,
    bg="blue",
    fg="yellow",
)

center_start_button = tkinter.Button(
    text="Center",
    width=10,
    height=2,
    bg="blue",
    fg="yellow",
)

random_start_button.bind("<Button-1>",random_start)
center_start_button.bind("<Button-1>",center_start)

welcome_message = tkinter.Label(text = "Select simulation mode:")

welcome_message.pack()

random_start_button.pack()

center_start_button.pack()

root_tk.mainloop()