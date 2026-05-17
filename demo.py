from display import Display
from counting import results
from survey import main


def main():
    my_display = Display()
    my_display.root.mainloop()
    results()


if __name__ == "__main__":
    main()
