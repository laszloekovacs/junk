from blessed import Terminal
import time

term = Terminal()

def main():
    subsystems = [
        "Warp Drive",
        "Shield Generator",
        "Life Support",
        "Navigation System",
        "Communication Array",
        "Sensor Suite",
        "Weapons System",
        "Reactor Core",
        "Auxiliary Power",
        "Emergency Systems",
    ]

    with term.fullscreen(), term.hidden_cursor():
        print(term.home + term.clear)

    print(term.blink("insewrt disk"))

    input("Press Enter to continue...")



if __name__ == "__main__":
    main()
