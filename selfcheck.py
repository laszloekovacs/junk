from blessed import Terminal
import time

term = Terminal()

def main():
    with term.fullscreen(), term.hidden_cursor():
        print(term.home + term.clear)
        width = 20
        height = 10
        x_start = (term.width - width) // 2
        y_start = (term.height - height) // 2

        for percentage in range(0, 101):
            print(term.move_xy(x_start - 5, y_start - 2) + f"Loading: {percentage}%")
            filled_width = int(width * (percentage / 100))

            for y in range(height):
                for x in range(width):
                    if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                        print(term.move_xy(x_start + x, y_start + y) + term.blue_on_blue + " " + term.normal)
                    elif x < filled_width:
                        print(term.move_xy(x_start + x, y_start + y) + term.white_on_white + " " + term.normal)
                    else:
                        print(term.move_xy(x_start + x, y_start + y) + " ")
            time.sleep(0.02)

        for y in range(height):
            for x in range(width):
                print(term.move_xy(x_start + x, y_start + y) + term.white_on_white + " " + term.normal)

        print(term.move_xy(x_start - 5, y_start + height + 2) + "Done!")
        term.inkey()

if __name__ == "__main__":
    main()
