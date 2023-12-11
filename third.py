import tkinter as tk
"""The main file to make a love note and the components of it"""
class LoveNote:
    def __init__(self, root):
        self.root = root
        self.root.title("Love Letter Generator")
        self.root.config(bg="gray", cursor="heart")

        self.create_widgets()

    def generate_love_letter(self):
        crush_name = self.crush_name_entry.get()
        date = self.date_entry.get()
        ending = self.ending_entry.get()

        love_letter = f"Dear {crush_name},\n\nI hope this letter finds you well. Today, {date}, I wish to pour my heart out. I hope you're well and healthy, living life with no regrets and with lots of sunshine.\n\n"
        love_letter += f"YEven after dark night. With this letter I hope you can come to understand me, the way I do you. {ending}\n\n"
        love_letter += "Yours sincerely,\n[Your Name]"

        with open("../love_letter.txt", "w") as file:
            file.write(love_letter)

        self.result_label.config(text="Love letter generated and saved to 'love_letter.txt'")

    def create_widgets(self):
        self.crush_name_label = tk.Label(self.root, text="Crush's Name:")
        self.crush_name_label.pack()

        self.crush_name_entry = tk.Entry(self.root)
        self.crush_name_entry.pack()

        self.date_label = tk.Label(self.root, text="Date:")
        self.date_label.pack()

        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        self.ending_label = tk.Label(self.root, text="Ending:")
        self.ending_label.pack()

        self.ending_entry = tk.Entry(self.root)
        self.ending_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.generate_love_letter)
        self.submit_button.pack()
