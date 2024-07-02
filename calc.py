import tkinter as tk

# Function to update the display when a button is clicked
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + number)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to perform calculation
def calculate():
    try:
        expression = display.get()
        result = eval(expression)  # Using eval() for simplicity, but consider security implications
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display
display = tk.Entry(root, width=20, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
button_1 = tk.Button(root, text="1", padx=20, pady=10, command=lambda: button_click("1"))
button_2 = tk.Button(root, text="2", padx=20, pady=10, command=lambda: button_click("2"))
button_3 = tk.Button(root, text="3", padx=20, pady=10, command=lambda: button_click("3"))
button_4 = tk.Button(root, text="4", padx=20, pady=10, command=lambda: button_click("4"))
button_5 = tk.Button(root, text="5", padx=20, pady=10, command=lambda: button_click("5"))
button_6 = tk.Button(root, text="6", padx=20, pady=10, command=lambda: button_click("6"))
button_7 = tk.Button(root, text="7", padx=20, pady=10, command=lambda: button_click("7"))
button_8 = tk.Button(root, text="8", padx=20, pady=10, command=lambda: button_click("8"))
button_9 = tk.Button(root, text="9", padx=20, pady=10, command=lambda: button_click("9"))
button_0 = tk.Button(root, text="0", padx=20, pady=10, command=lambda: button_click("0"))

button_add = tk.Button(root, text="+", padx=20, pady=10, command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=20, pady=10, command=lambda: button_click("/"))
button_decimal = tk.Button(root, text=".", padx=20, pady=10, command=lambda: button_click("."))
button_clear = tk.Button(root, text="C", padx=20, pady=10, command=clear_display)
button_equals = tk.Button(root, text="=", padx=20, pady=10, command=calculate)

# Grid buttons on the window
button_clear.grid(row=1, column=0)
button_divide.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_subtract.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_add.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_decimal.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_equals.grid(row=4, column=3)

button_0.grid(row=5, column=0, columnspan=2)
root.mainloop()
