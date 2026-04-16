import tkinter as tk
import turtle


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
            bg="magenta",
        )
        self.interface_frame.grid(row=1, column=0)

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
        t = turtle.RawTurtle(self.action_canvas)
        return t


def move_left(t):
    t.left(90)
    t.forward(10)


def move_right(self):
    self.right(90)
    self.forward(10)


def move_forward(self):
    self.forward(10)


def main():
    my_display = Display()
    my_display.root.mainloop()


if __name__ == "__main__":
    main()


# # Setup
# screen = turtle.Screen()
# t = turtle.Turtle()


# # Define movement functions
# def move_left():
#     t.left(90)
#     t.forward(10)


# def move_right():
#     t.right(90)
#     t.forward(10)


# def move_forward():
#     t.forward(10)


# # Assign keys to functions
# screen.onkey(move_left, "Left")  # Press Left arrow to move left
# screen.onkey(move_right, "Right")  # Press Right arrow to move right
# screen.onkey(move_forward, "Up")  # Press Up arrow to move forward
# screen.listen()

# screen.mainloop()
