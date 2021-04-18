from tkinter import *
from PIL import ImageTk, Image

window = Tk()

class ZoomClass():
     def __init__(self, title, time, link,):

frame_title = Frame()
frame_list = Frame()


image1 = Image.open("zoomer_icon128.png")
test = ImageTk.PhotoImage(image1)

label1 = Label(master=frame_title, image=test)
label1.image = test
label1.pack()

label_a = Label(master=frame_title, text="I'm in Frame A")
label_a.pack()

label_b = Label(master=frame_list, text="I'm in Frame B")
label_b.pack()

frame_title.pack()
frame_list.pack()

window.mainloop()