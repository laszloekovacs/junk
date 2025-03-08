from blessed import Terminal
import time
import textwrap

term = Terminal()

def main():
    with term.fullscreen(), term.hidden_cursor():
        print(term.home + term.clear)
        lorem_ipsum = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. 
        Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. 
        Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. 
        Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. 
        Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. 
        Pellentesque congue. Ut in risus volutpat libero pharetra tempor. 
        Cras vestibulum bibendum augue. Praesent egestas leo in pede. 
        Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. 
        Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; 
        Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.
        """
        wrapped_text = textwrap.fill(lorem_ipsum, width=term.width)
        print(wrapped_text)
        time.sleep(1)

        lines = wrapped_text.split('\n')
        for line_num, line in enumerate(lines):
            for char_num, _ in enumerate(line):
                print(term.move_xy(char_num, line_num) + term.black_on_black + " " + term.normal, end='', flush=True)
                time.sleep(0.005)

        term.inkey()

if __name__ == "__main__":
    main()
