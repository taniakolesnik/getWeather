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


def test_function(entry):
   print(entry)


# frame top
frame_top = Frame(root, bg='#80c1ff', bd=5)
frame_top.place(rely=0.03, relx=0.5, relwidth=0.95, height=45, anchor='n')

entry = Entry(frame_top)
entry.place(rely=0.2, relheight=0.6, relwidth=0.75)

# frame result
frame_result = Frame(root, bg='#80c1ff', bd=5)
frame_result.place(y=80, relx=0.5, relwidth=0.95, height=300, anchor='n')
result = Label(frame_result).place(relwidth=1, relheight=1)

button = Button(frame_top, text="Get Weather", command=lambda: test_function(entry.get()))
button.place(rely=0.2, relheight=0.6, relwidth=0.2, relx=0.8)

# frame error if any
frame_error = Frame(root, bg='#80c1ff', bd=5)
frame_error.place(y=450, relx=0.5, relwidth=0.95, height=50, anchor='s')
error = Label(frame_error).place(relwidth=1, relheight=1)

root.minsize(width=WIDTH, height=HEIGHT)
root.maxsize(width=WIDTH, height=HEIGHT)
root.mainloop()
