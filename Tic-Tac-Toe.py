# Adding the Libraries
from tkinter import *

# Initializing the window
root = Tk()
root.title("Tic-Tac-Toe Game")
field = Canvas(root, width=600, height=600)
field.pack()
font_turn = "Times 20 italic bold"
font_marker = "Times 60 italic bold"
tell_whose_turn = field.create_text(300, 20, fill="darkblue", font=font_turn,
                                    text="@ Turn to click")

# Global variables for the game
turn = 1
game_field = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

# Draw the lines
field.create_line(200, 50, 200, 550)
field.create_line(400, 50, 400, 550)
field.create_line(50, 200, 550, 200)
field.create_line(50, 400, 550, 400)

##################################################
############## The needed Functions ##############
##################################################

# For detecting mouse click for playing
def click(event):
    global turn, game_field
    if turn%2 == 1:
        text = "@"
        color = "brown"
    elif turn%2 == 0:
        text = "#"
        color = "darkcyan"

    # Check if the player clicked on ther proper field
    if event.x>60 and event.x<190:
        if event.y>60 and event.y<190:
            if game_field[0][0] != 0:
                return
            else:
                game_field[0][0] = text
                add_marker(125, 125, text, color)
        elif event.y>210 and event.y<390:
            if game_field[0][1] != 0:
                return
            else:
                game_field[0][1] = text
                add_marker(125, 300,text, color)
        elif event.y>410 and event.y<540:
            if game_field[0][2] != 0:
                return
            else:
                game_field[0][2] = text
                add_marker(125, 475, text, color)
        else:
            return
    elif event.x>210 and event.x<390:
        if event.y>60 and event.y<190:
            if game_field[1][0] != 0:
                return
            else:
                game_field[1][0] = text
                add_marker(300, 125, text, color)
        elif event.y>210 and event.y<390:
            if game_field[1][1] != 0:
                return
            else:
                game_field[1][1] = text
                add_marker(300, 300, text, color)
        elif event.y>410 and event.y<540:
            if game_field[1][2] != 0:
                return
            else:
                game_field[1][2] = text
                add_marker(300, 475, text, color)
        else:
            return
    elif event.x>410 and event.x<540:
        if event.y>60 and event.y<190:
            if game_field[2][0] != 0:
                return
            else:
                game_field[2][0] = text
                add_marker(475, 125, text, color)
        elif event.y>210 and event.y<390:
            if game_field[2][1] != 0:
                return
            else:
                game_field[2][1] = text
                add_marker(475, 300, text, color)
        elif event.y>410 and event.y<540:
            if game_field[2][2] != 0:
                return
            else:
                game_field[2][2] = text
                add_marker(475, 475, text, color)
        else:
            return
    else:
        return

    turn +=1
    change_turn()

# For telling the players whose turn it is
def change_turn():
    global turn, tell_whose_turn, font_turn
    if turn%2 == 0:
        field.delete(tell_whose_turn)
        tell_whose_turn = field.create_text(300, 20, fill="darkblue", font=font_turn,
                                            text="# Turn to click")

    elif turn%2 == 1:
        field.delete(tell_whose_turn)
        tell_whose_turn = field.create_text(300, 20, fill="darkblue", font=font_turn,
                                            text="@ Turn to click")

# For adding Signs in the game field
def add_marker(x, y, txt, color):
    global font_marker
    field.create_text(x, y, fill=color, font=font_marker,
                      text=txt)

# For checking if a player has won the game
def check_win():
    pass

##################################################
##################################################
##################################################


# The loop of the game
field.bind("<Button-1>", click)
field.pack()

root.mainloop()