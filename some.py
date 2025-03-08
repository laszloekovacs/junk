from blessed import Terminal
from blessed.sequences import Sequence
from term_image.image import from_file
import time

term = Terminal()

def main():
    options = ["Option 1", "Option 2", "Option 3", "Quit"]
    current_selection = 0
    blink_on = True  # Initialize blinking state

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        print(term.home + term.clear)
        
        try:
            image = from_file("hand.jpg")
            print(image)
        except Exception as e:
            print(f"Error displaying image: {e}")
            print("Please ensure 'hand.jpg' exists in the same directory.")

        while True:
            print(term.move_xy(0, 0) + term.clear_eol + "Select an option:")
            for i, option in enumerate(options):
                if i == current_selection:
                    if blink_on:
                        print(term.move_xy(0, i + 1) + term.reverse + option + term.normal)
                    else:
                        print(term.move_xy(0, i + 1) + option)  # No highlighting when blinking off
                else:
                    print(term.move_xy(0, i + 1) + option)

            key = term.inkey(timeout=0.5)  # Check for keypress with timeout
            
            # Toggle blink state every half second
            blink_on = not blink_on

            if key:  # If a key was pressed
                if key.name == "KEY_DOWN":
                    current_selection = (current_selection + 1) % len(options)
                elif key.name == "KEY_UP":
                    current_selection = (current_selection - 1) % len(options)
                elif key.name == "KEY_ENTER":
                    if options[current_selection] == "Quit":
                        print(term.move_xy(0, len(options) + 2) + "Exiting...")
                        break
                    else:
                        print(term.move_xy(0, len(options) + 2) + f"You selected: {options[current_selection]}")
                        break
                elif key.name == "KEY_ESCAPE":
                    print(term.move_xy(0, len(options) + 2) + "Exiting...")
                    break

if __name__ == "__main__":
    main()
