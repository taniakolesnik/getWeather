from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = HEIGHT
root = tk.Tk()
filename = 'C:\\Users\\TanyaK\\PycharmProjects\\Weather\\image.jpg'

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

PILFile = Image.open('image.jpg')
image = ImageTk.PhotoImage(PILFile)
canvas.create_image(0, 0, image=image, anchor=NW)

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(rely=0.03, relx=0.5, relwidth=0.95, relheight=0.1, anchor='n')

entry = Entry(frame)
entry.place(rely=0.2, relheight=0.6, relwidth=0.75)

button = Button(frame, text="Get Weather")
button.place(rely=0.2, relheight=0.6, relwidth=0.2, relx=0.8)

root.minsize(width=WIDTH, height=HEIGHT)
root.maxsize(width=WIDTH, height=HEIGHT)
root.mainloop()
