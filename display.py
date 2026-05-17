import tkinter as tk
import turtle
from survey import *
from counting import results

question_file = "questions.txt"
answer_options = "answer_options.csv"
answer_file = "responses.txt"

question_list = get_question(question_file)
answer_options_list = get_answer_options(answer_options_file)


class Display:
    def __init__(self):
        self.current_question = 0
        self.root = tk.Tk()
        self.init_window()
        self.create_interface_frame()
        self.create_turtle_frame()
        self.create_turtle_canvas()
        self.create_buttons()

    def init_window(self):
        self.root.title("The Adventures of the Turtle")
        self.screen_size = (800, 600)
        self.root.geometry(f"{self.screen_size[0]}x{self.screen_size[1]}")

    def create_interface_frame(self):
        self.interface_frame = tk.Frame(
            self.root, width=self.screen_size[0], height=(0.25 * self.screen_size[1])
        )
        self.interface_frame.grid(row=1, column=0)

    def create_buttons(self):

        self.a = tk.Button(
            self.interface_frame,
            text=answer_options_list[self.current_question][0],
            font="Garamond 12",
            command=self.move_left,
        )
        self.a.grid(row=0, column=0)

        self.b = tk.Button(
            self.interface_frame,
            text=answer_options_list[self.current_question][1],
            font="Garamond 12",
            command=self.move_forward,
        )
        self.b.grid(row=0, column=1)

        self.c = tk.Button(
            self.interface_frame,
            text=answer_options_list[self.current_question][2],
            font="Garamond 12",
            command=self.move_right,
        )
        self.c.grid(row=0, column=2)

        self.text = tk.Label(
            self.interface_frame,
            text=str(ask_question(question_list, answer_options_list)),
            font="Garamond 12",
        )
        self.text.grid(row=0, column=0)

    def create_turtle_frame(self):
        self.turtle_frame_height = 0.75 * self.screen_size[1]
        self.turtle_frame_width = self.screen_size[0]
        self.turtle_frame = tk.Frame(
            self.root,
            width=self.turtle_frame_width,
            height=self.turtle_frame_height,
        )
        self.turtle_frame.grid(row=0, column=0)

    def create_turtle_canvas(self):
        self.action_canvas = tk.Canvas(
            self.turtle_frame,
            width=self.turtle_frame_width,
            height=self.turtle_frame_height,
        )
        self.action_canvas.pack()
        self.turtle_screen = turtle.TurtleScreen(self.action_canvas)
        self.turtle_screen.bgcolor("DarkGreen")
        self.t = turtle.RawTurtle(self.turtle_screen)

        self.t.setheading(90)
        self.t.penup()
        self.t.setpos(0, -0.4 * (self.turtle_frame_height))

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(question_list):
            self.text.config(text = question_list[self.current_question])
            self.a.config(text = answer_options_list[self.current_question][0])
            self.b.config(text = answer_options_list[self.current_question][1])
            self.c.config(text = answer_options_list[self.current_question][2])
        else:
            self.a.grid_remove()
            self.b.grid_remove()
            self.c.grid_remove()
            self.text.config(text = results())

    def move_left(self):
        self.t.left(90)
        self.t.forward(20)
        self.t.right(90)
        save_answers("A")
        self.next_question()

    def move_right(self):
        self.t.right(90)
        self.t.forward(20)
        self.t.left(90)
        save_answers("C")
        self.next_question()

    def move_forward(self):
        self.t.forward(20)
        save_answers("B")
        self.next_question()

    def connect_keys(self):
        self.turtle_screen.onkey(self.move_left, "Left")
        self.turtle_screen.onkey(self.move_right, "Right")
        self.turtle_screen.onkey(self.move_forward, "Up")
        self.turtle_screen.listen()
