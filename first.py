import tkinter as tk
from second import LoveCalculatorApp
from third import LoveNote
from fourth import Factorial

"""The main file where everything gets compiled here. This file pulls from the others"""

class IntroWidget(LoveCalculatorApp, LoveNote, Factorial):
    def __init__(self, root):
        self.root = root
        self.root.title("101 Girl Games")
        self.root.geometry("450x250")
        self.root.config(bg="purple", cursor="heart")

        self.label1 = tk.Label(self.root, text="Welcome to the 101 Girl Games program. Before we begin, enter your name:", bg="lightblue")
        self.label1.pack(pady=5)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.name_saved_button = tk.Button(self.root, text="Click me to save the name!", command=self.button_clicked)
        self.name_saved_button.pack(pady=8)

        self.label2 = tk.Label(self.root, text="Choose one of the following options to play a game you would like!", bg="lightblue")
        self.label2.pack(pady=5)

        options = [("Love Calculator", 1), ("Love Letter", 2), ("Numbers", 3)]

        for text, option in options:
            button = tk.Button(self.root, text=text, command=lambda o=option: self.on_option_selected(o))
            button.pack(pady=5)

    def button_clicked(self):
        user_name = self.name_entry.get()
        print(f"Your name, {user_name}, has been saved")

    def on_option_selected(self, selected_option):
        if selected_option == 1:
            # If "Love Calculator" is selected, create and show LoveCalculatorApp
            love_calculator_root = tk.Toplevel(self.root)
            love_calculator_app = LoveCalculatorApp(love_calculator_root)
        elif selected_option == 2:
            love_note_root = tk.Toplevel(self.root)
            love_note_app = LoveNote(love_note_root)
        elif selected_option == 3:
            factorial_root = tk.Toplevel(self.root)
            factorial_app = Factorial(factorial_root)
        else:
            print(f"Option {selected_option}: A new window will open to play the game!")
    # activating the games



def main():
    root = tk.Tk()
    app = IntroWidget(root)
    root.mainloop()


if __name__ == "__main__":
    main()
