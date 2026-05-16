import tkinter as tk
import turtle
from survey import get_question, ask_question, save_answers

question_file = "questions.txt"
answer_options = "answer_options.csv"
answer_file = "responses.txt"


question_list = get_question(question_file)


class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.init_window()
        self.create_interface_frame()
        self.create_turtle_frame()
        self.create_turtle_canvas()

    def init_window(self):
        self.root.title("Name")
        self.screen_size = (800, 600)
        self.root.geometry(f"{self.screen_size[0]}x{self.screen_size[1]}")

    def create_interface_frame(self):
        self.interface_frame_height = 100
        self.interface_frame = tk.Frame(
            self.root,
            width=self.screen_size[0],
            height=self.interface_frame_height,
        )
        self.interface_frame.grid(row=1, column=0)

        self.a = tk.Button(
            self.interface_frame,
            text="Option A",
            font="Garamond 12",
            command=self.move_left,
        )
        self.a.grid(row=0, column=0)

        self.b = tk.Button(
            self.interface_frame,
            text="Option B",
            font="Garamond 12",
            command=self.move_forward,
        )
        self.b.grid(row=0, column=1)

        self.c = tk.Button(
            self.interface_frame,
            text="Option C",
            font="Garamond 12",
            command=self.move_right,
        )
        self.c.grid(row=0, column=2)

    def create_text_frame(self):
        self.text_frame_height = 100
        self.text_frame = tk.Frame(
            self.root,
            width=self.screen_size[0],
            height=self.text_frame_height,
            bg="blue",
        )
        self.interface_frame.grid(row=2, column=0)

    def create_turtle_frame(self):
        self.turtle_frame_height = self.screen_size[1] - self.interface_frame_height
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

    def move_left(self):
        self.t.left(90)
        self.t.forward(10)
        self.t.right(90)
        save_answers("A")

    def move_right(self):
        self.t.right(90)
        self.t.forward(10)
        self.t.left(90)
        save_answers("C")

    def move_forward(self):
        self.t.forward(10)
        save_answers("B")

    def connect_keys(self):
        self.turtle_screen.onkey(self.move_left, "Left")
        self.turtle_screen.onkey(self.move_right, "Right")
        self.turtle_screen.onkey(self.move_forward, "Up")
        self.turtle_screen.listen()
