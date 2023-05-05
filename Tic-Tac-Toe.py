# Adding the Libraries
from tkinter import *
from math import radians

# Initializing the window
root = Tk()
root.title("Tic-Tac-Toe Game")
root.resizable(False, False)
field = Canvas(root, width=600, height=600)
field.configure(bg="#dce2e5")
field.pack()
font_turn = "Times 20 italic bold"
font_end = "Times 30 italic bold"
font_marker = "Times 60 italic bold"
tell_whose_turn = field.create_text(300, 20, fill="darkblue", font=font_turn,
                                    text="@ Turn to click")

# Global variables for the game
end_game = False
turn = 1
game_field = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

# Draw the lines
field.create_line(200, 50, 200, 550)
field.create_line(400, 50, 400, 550)
field.create_line(50, 200, 550, 200)
field.create_line(50, 400, 550, 400)

# Create a Button to Exit
exit_button = Button(root, text = 'Exit \U0001f614', bd = '6', font="10",
             command = root.destroy)
# Set the position of button on the left of the text, on top  
exit_button.place(x=113, y=2)

# Create a Button to Reset
reset_button = Button(root, text = 'Reset \U0001f600', bd = '6', font="10",
             command = lambda: again())
# Set the position of button on the left of the text, on top  
reset_button.place(x=415, y=2)

##################################################################
###################### The needed Functions ######################
##################################################################

# For detecting mouse click for playing
def click(event):
    global turn, game_field, end_game
    if end_game:
        return
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

    check_win()
    if end_game:
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
    for i in range(3):
        if game_field[i][0]==game_field[i][1]==game_field[i][2] != 0:
            win_or_draw(175*i+125-2, 75, 175*i+125+2, 525, game_field[i][0])
        elif game_field[0][i]==game_field[1][i]==game_field[2][i] != 0:
            win_or_draw(75, 175*i+125-2, 525, 175*i+125+2, game_field[0][i])
    if game_field[0][0]==game_field[1][1]==game_field[2][2] != 0:
        win_or_draw(74, 76, 526, 524, game_field[1][1], sloped=1)
    elif game_field[2][0]==game_field[1][1]==game_field[0][2] != 0:
        win_or_draw(74, 524, 526, 76, game_field[1][1], sloped=1)
    elif sum([row.count(0) for row in game_field])==0:
        win_or_draw(winner="draw")

# Tell if a player won or it's a draw
def win_or_draw(x1=75, y1=175, x2=525, y2=475, winner="draw", sloped=0):
    global tell_whose_turn, end_game
    if end_game:
        return
    else:
        end_game = True
    color = {"@": "brown",
             "#": "darkcyan"}
    if winner=="draw":
        field.delete(tell_whose_turn)
        field.create_text(300, 20, fill="black", font=font_end,
                          text="---"+winner+"---")
    else:
        if sloped==0:
            field.delete(tell_whose_turn)
            field.create_text(300, 20, fill=color[winner], font=font_end,
                              text=winner+" has WON!")
            field.create_rectangle(x1, y1, x2, y2, fill=color[winner], outline=color[winner])
        else:
            field.delete(tell_whose_turn)
            field.create_text(300, 20, fill=color[winner], font=font_end,
                              text=winner+"has WON!")
            # create the rectangle as a polygon
            field.create_polygon(x1, y1, y1, x1, x2, y2, y2, x2, fill=color[winner], outline=color[winner])

def again():
    global turn, game_field, tell_whose_turn, end_game
    game_field = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
    end_game = False
    
    # Delete all & initiate the field again
    field.delete("all")
    tell_whose_turn = field.create_text(300, 20, fill="darkblue", font=font_turn,
                                    text="@ Turn to click")
    field.create_line(200, 50, 200, 550)
    field.create_line(400, 50, 400, 550)
    field.create_line(50, 200, 550, 200)
    field.create_line(50, 400, 550, 400)

##################################################################
##################################################################
##################################################################


# The loop of the game
field.bind("<Button-1>", click)
field.pack()

root.mainloop()