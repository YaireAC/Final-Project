import tkinter as tk

"""This is the main file for Option 1 game."""
class LoveCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Love Calculator")
        self.root.config(bg="pink", cursor="heart")

        # Create and place widgets
        self.label_name1 = tk.Label(self.root, text="Enter Name 1:")
        self.label_name1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_name1 = tk.Entry(self.root)
        self.entry_name1.grid(row=0, column=1, padx=10, pady=5)

        self.label_name2 = tk.Label(self.root, text="Enter Name 2:")
        self.label_name2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_name2 = tk.Entry(self.root)
        self.entry_name2.grid(row=1, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate Love", command=self.calculate_love)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.root, text="Love Percentage: ")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.grid(row=4, column=0, columnspan=2)

    def calculate_love(self):
        name1 = self.entry_name1.get()
        name2 = self.entry_name2.get()

        # Calculate the love percentage
        total_characters = len(name1) + len(name2)
        love_percent = int(total_characters * 2)

        # Making sure the percentage is between 1 and 100
        love_percent = min(100, max(1, love_percent))

        # Changing label with the love percentage
        self.result_label.config(text=f"Love Percentage: {love_percent}%")

        # ing a heart with the calculated size
        self.canvas.delete("all")
        heart_size = love_percent * 2
        self.canvas.create_text(150, 150, text="❤", font=("Arial", heart_size))

