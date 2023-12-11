import tkinter as tk

class Factorial():

    """calculating some math to display through tk"""

    def __init__(self, root):
        self.root = root
        self.root.title("Factorial Maker")
        self.root.geometry("450x250")
        self.root.config(bg="light green", cursor="heart")

        self.label_name1 = tk.Label(self.root, text="Enter Your number:")
        self.label_name1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        self.number = tk.Entry(self.root)
        self.number.grid(row=0, column=1, padx=10, pady=5)

        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, state='readonly')
        self.result_entry.grid(row=1, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate Factorial", command=self.calculate_factorial)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def calculate_factorial(self):
        try:
            num = int(self.number.get())
            result = self.factorial(num)
            self.result_var.set(result)
        except ValueError:
            self.result_var.set("Invalid input. Go ahead and try again")
