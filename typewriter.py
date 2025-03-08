from blessed import Terminal
import time

term = Terminal()

def typewriter_effect(text, delay=0.05):
    """Prints text with a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line at the end

def main():
    with term.fullscreen(), term.hidden_cursor():
        print(term.home + term.clear)
        typewriter_effect("This is a typewriter effect using the blessed library.", 0.05)
        typewriter_effect("It simulates the typing of text.", 0.03)
        typewriter_effect("Each character appears one by one.", 0.07)
        typewriter_effect("Press any key to exit...", 0.02)
        term.inkey()

if __name__ == "__main__":
    main()
