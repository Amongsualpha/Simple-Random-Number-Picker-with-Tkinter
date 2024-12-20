import tkinter as tk
import random

class RandomNumberPicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Number Picker")

        # Range inputs for minimum and maximum values
        self.min_label = tk.Label(root, text="Minimum:")
        self.min_label.pack()
        self.min_entry = tk.Entry(root)
        self.min_entry.pack()

        self.max_label = tk.Label(root, text="Maximum:")
        self.max_label.pack()
        self.max_entry = tk.Entry(root)
        self.max_entry.pack()

        # Button to pick a random number
        self.pick_button = tk.Button(root, text="Pick a Number", command=self.pick_number)
        self.pick_button.pack(pady=10)

        # Label to display the picked number
        self.result_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.result_label.pack()

    def pick_number(self):
        try:
            # Get min and max values from the entries
            min_value = int(self.min_entry.get())
            max_value = int(self.max_entry.get())
            
            # Check if min is less than max
            if min_value > max_value:
                self.result_label.config(text="Invalid range")
                return
            
            # Pick a random number within the specified range
            random_number = random.randint(min_value, max_value)
            self.result_label.config(text=f"Picked Number: {random_number}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")

# Create the main window and start the app
root = tk.Tk()
app = RandomNumberPicker(root)
root.mainloop()
