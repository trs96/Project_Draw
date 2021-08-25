import tkinter as tk
import random

def make_segment():
    return [random.randrange(0, 1000) for _ in range(4)]


def draw_random_lines():
    canvas.create_line(*make_segment())
    root.after(1, draw_random_lines)

root = tk.Tk()
canvas = tk.Canvas(root, height=1000, width=1000)
canvas.pack()

draw_random_lines()
root.mainloop()