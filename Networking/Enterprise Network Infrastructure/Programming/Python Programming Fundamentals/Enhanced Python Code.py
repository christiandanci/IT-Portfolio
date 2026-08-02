import tkinter as tk
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate(operation, num1, num2):
    """
    Perform a mathematical operation on two numbers.
    Uses a dictionary-based dispatching system for scalability.
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    
    result = operations.get(operation, lambda x, y: "Invalid Operation")(num1, num2)
    logging.info(f"Operation: {operation}, Num1: {num1}, Num2: {num2}, Result: {result}")
    return result

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator")

        # Creating input fields
        self.entry1 = self.create_entry(row=0, column=1)
        self.entry2 = self.create_entry(row=1, column=1)

        # Labels for input
        tk.Label(root, text="Number 1:").grid(row=0, column=0)
        tk.Label(root, text="Number 2:").grid(row=1, column=0)

        # Creating buttons dynamically
        self.create_button("Add", "add", 2, 0)
        self.create_button("Subtract", "subtract", 2, 1)
        self.create_button("Multiply", "multiply", 3, 0)
        self.create_button("Divide", "divide", 3, 1)

        # Result Label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=4, columnspan=2)

    def create_entry(self, row, column):
        """Creates and returns a Tkinter entry field"""
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=column)
        return entry

    def create_button(self, text, operation, row, column):
        """Creates buttons dynamically for each operation"""
        button = tk.Button(self.root, text=text, command=lambda: self.on_calculate(operation))
        button.grid(row=row, column=column)

    def on_calculate(self, operation):
        """Handles calculation and updates result label"""
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = calculate(operation, num1, num2)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Error: Invalid Input")

# Tkinter GUI Loop
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
