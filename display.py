import tkinter as tk
import turtle


class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.init_window()
        self.create_turtle_frame()
        # self.create_interface_frame()

    def init_window(self):
        self.root.title("Name")
        self.screen_size = (800, 600)
        self.root.geometry(f"{self.screen_size[0]}x{self.screen_size[1]}")

        self.interface_frame_height = 100
        self.interface_frame = tk.Frame(
            self.root,
            width=self.screen_size[0],
            height=self.interface_frame_height,
        )
        self.interface_frame.grid(row=1, column=0)

        self.turtle_frame_height = self.screen_size[1] - self.interface_frame_height
        self.turtle_frame_width = self.screen_size[0]
        self.turtle_frame = tk.Frame(
            self.root,
            width=self.turtle_frame_width,
            height=self.turtle_frame_height,
        )
        self.turtle_frame.grid(row=0, column=0)

    def create_turtle_frame(self):
        self.action_canvas = tk.Canvas(
            self.turtle_frame,
            width=self.turtle_frame_width,
            height=self.turtle_frame_height,
        )
        self.action_canvas.pack()
        t = turtle.RawTurtle(self.action_canvas)


def main():
    my_display = Display()
    my_display.root.mainloop()
