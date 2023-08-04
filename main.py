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
    
    def __init__(self):
        
        x = random.randint(0, ((GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE)
        y = random.randint(0, ((GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE)

        self.coordinates = [x,y]

        canvas.create_rectangle(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="foood")


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

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack() 

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

window.mainloop()