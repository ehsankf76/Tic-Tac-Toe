# Adding the Libraries
from tkinter import *

# Initializing the window
root = Tk()
root.title("Tic-Tac-Toe Game")
field = Canvas(root, width=600, height=600)
field.pack()

turn = 1
j = field.create_text(300, 20, fill="darkblue", font="Times 20 italic bold",
                      text="@ Turn to click")

# Draw the lines
field.create_line(200, 50, 200, 550)
field.create_line(400, 50, 400, 550)
field.create_line(50, 200, 550, 200)
field.create_line(50, 400, 550, 400)

def click(event):
    global turn

    # Check if the player clicked on ther proper field
    if event.x>60 and event.x<190:
        if event.y>60 and event.y<190:
            pass
        elif event.y>210 and event.y<390:
            pass
        elif event.y>410 and event.y<540:
            pass
        else:
            return
    elif event.x>210 and event.x<390:
        if event.y>60 and event.y<190:
            pass
        elif event.y>210 and event.y<390:
            pass
        elif event.y>410 and event.y<540:
            pass
        else:
            return
    elif event.x>410 and event.x<540:
        if event.y>60 and event.y<190:
            pass
        elif event.y>210 and event.y<390:
            pass
        elif event.y>410 and event.y<540:
            pass
        else:
            return
    else:
        return

    print(event.x, event.y)
    change_turn()
    turn +=1

def change_turn():
    global turn, j
    if turn%2 == 0:
        field.delete(j)
        j = field.create_text(300, 20, fill="darkblue", font="Times 20 italic bold",
                              text="# Turn to click")

    elif turn%2 == 1:
        field.delete(j)
        j = field.create_text(300, 20, fill="darkblue", font="Times 20 italic bold",
                              text="@ Turn to click")

def check_win():
    pass

field.bind("<Button-1>", click)
field.pack()

root.mainloop()