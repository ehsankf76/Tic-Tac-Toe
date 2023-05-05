# Adding the Libraries
from tkinter import *

# Initializing the window
root = Tk()
root.title("Tic-Tac-Toe Game")
field = Canvas(root, width=600, height=600)
field.pack()

j = field.create_text(300, 20, fill="darkblue", font="Times 20 italic bold",
                        text="@ Turn to click")

# Draw the lines
field.create_line(200, 50, 200, 550)
field.create_line(400, 50, 400, 550)
field.create_line(50, 200, 550, 200)
field.create_line(50, 400, 550, 400)

def click(event):
    pass

def change_turn():
    pass

def check_win():
    pass

field.bind("<Button-1>", click)
field.pack()

root.mainloop()