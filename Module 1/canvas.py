from tkinter import *

# Create the main window
root = Tk()
root.title("Square on Canvas")
root.geometry("400x400")

# Create a canvas
canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=20)

# Draw a square
canvas.create_rectangle(
    50, 50, 150, 150, fill="lightblue", outline="black", width=2)

# Run the application
root.mainloop()
