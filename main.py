from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 30
SPACE_SIZE = 40
BODY_PARTS = 3
SNAKE_COLOR = "yellow"
FOOD_COLOR = "WHITE"
BACKGROUND_COLOR = "BLACK"



class Snake():
    pass

class Food():
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("SnakeS")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 35))
label.pack()


window.mainloop()