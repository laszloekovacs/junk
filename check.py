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
        y_offset = term.height // 2 - len(subsystems) // 2
        x_offset = term.width // 2 - max(len(s) for s in subsystems) // 2
        
        for _ in range(10):
            for i, subsystem in enumerate(subsystems):
                print(term.move_xy(x_offset, y_offset + i) + term.blink + subsystem + term.normal)
            time.sleep(0.1)
            for i, subsystem in enumerate(subsystems):
                print(term.move_xy(x_offset, y_offset + i) + subsystem)
            time.sleep(0.1)

        for i, subsystem in enumerate(subsystems):
            print(term.move_xy(x_offset, y_offset + i) + term.green + subsystem + term.normal)

        term.inkey()

if __name__ == "__main__":
    main()
