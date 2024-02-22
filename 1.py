from tkinter import *
from tkinter import simpledialog
import random
import time
class Ball:
    def __init__(self, canvas, paddle, score):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.id, 400, 400)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.show_game_over()
        if self.hit_paddle(pos) == True:
            self.y = -3
            self.score.increase_score()
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3 
    def show_game_over(self):
        self.canvas.create_text(
            self.canvas_width / 2,
            self.canvas_height / 2,
            text="You lost",
            font=("Helvetica", 30),
            fill="red"
        )
        tk.update_idletasks()
        tk.update()
        time.sleep(2)
        tk.destroy()
class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 150, 15, fill='blue')
        self.canvas.move(self.id, 350, 600)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0  
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self,evt):
            self.x = -3
    def turn_right(self,evt):
            self.x = 3
class Score:
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0
        self.id = self.canvas.create_text(10, 10, anchor="nw", text=f"Score: {self.score}", font=("Helvetica", 16), fill="black")
    def increase_score(self):
        self.score += 1
        self.draw()
    def draw(self):
        self.canvas.itemconfig(self.id, text="Score: {}".format(self.score))
        
tk = Tk()   
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=800, bd=0,
highlightthickness=0)
canvas.pack()   
tk.update()

paddle = Paddle(canvas)
score = Score(canvas)
ball = Ball(canvas, paddle, score)

while True:
    if ball.hit_bottom is False:
        ball.draw()
        paddle.draw()
        score.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)