from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = Tk()

class ZoomClass():

    def __init__(self, title, time, meeting_id, link):
         self.title = title
         self.time = time
         self.meeting_id = meeting_id
         self.link = link

    def create_frame(self, master=None):
        entireFrame = Frame(master=master)

        topFrame = Frame(master=entireFrame)
        labelTitle = Label(master=topFrame, text=self.title,font=('Arial', 25))
        labelTitle.pack()
        topFrame.pack()

        bottomFrame = Frame(master=entireFrame,borderwidth=3)

        leftSide = Label(master=bottomFrame,text=self.meeting_id).grid(column=0, row=0,columnspan=9, sticky='w')
        centerLine = Label(master=bottomFrame, text="|").grid(column=10,row=0, sticky='w')
        rightSide = Label(master=bottomFrame, text=self.time).grid(column=11,row=0,columnspan=9, sticky='w')
        # leftButtom.grid(column=0, row=0)
        # centerLine.grid(column=1, row=0)
        # rightSide.grid(column=2, row=0)

        # leftButtom.pack()
        # centerLine.pack()
        # rightSide.pack()

        # leftButtom.place(relx=0.5, rely=0.5, anchor="center")
        # centerLine.place(relx=0.5, rely=0.5, anchor="center")
        # rightSide.place(relx=0.5, rely=0.5, anchor="center")
        
        bottomFrame.pack()

        return entireFrame
        
# import tkinter as tk
# parent = tk.Tk()
# parent.title('Find & Replace')
# tk.Label(parent, text="Find:").grid(row=0, column=0, sticky='e')
# tk.Entry(parent, width=60).grid(row=0, column=1, padx=2, pady=2, sticky='we', columnspan=9)
# tk.Label(parent, text="Replace:").grid(row=1, column=0, sticky='e')
# tk.Entry(parent).grid(row=1, column=1, padx=2, pady=2, sticky='we',columnspan=9)
# tk.Button(parent, text="Find").grid( row=0, column=10, sticky='e' + 'w', padx=2, pady=2)
# tk.Button(parent, text="Find All").grid(row=1, column=10, sticky='e' + 'w', padx=2)
# tk.Button(parent, text="Replace").grid(row=2, column=10, sticky='e' +'w', padx=2)
# tk.Button(parent, text="Replace All").grid(row=3, column=10, sticky='e' + 'w', padx=2)
# tk.Checkbutton(parent, text='Match whole word only').grid(row=2, column=1, columnspan=4, sticky='w')
# tk.Checkbutton(parent, text='Match Case').grid(row=3, column=1, columnspan=4, sticky='w')
# tk.Checkbutton(parent, text='Wrap around').grid(row=4, column=1, columnspan=4, sticky='w')
# tk.Label(parent, text="Direction:").grid(row=2, column=6, sticky='w')
# tk.Radiobutton(parent, text='Up', value=1).grid(row=3, column=6, columnspan=6, sticky='w')
# tk.Radiobutton(parent, text='Down', value=2).grid(row=3, column=7, columnspan=2, sticky='e')
# parent.mainloop()


# image1 = Image.open("zoomer_icon128.png")
# test = ImageTk.PhotoImage(image1)

# label1 = Label(image=test)
# label1.image = test
# label1.pack()

appFrame = Frame(width=400, height=600)

zoomClass = ZoomClass("Title of Cal", "April some some\nsome thing er", "999 9999 9999", "https://weewf")
zoomFrame = zoomClass.create_frame(appFrame)
zoomFrame.pack()

appFrame.pack()

# canvas = Canvas(root, height=0, width=400, bg='#23314A', border=0)
# canvas.pack()

root.geometry("400x600")
root.resizable(False, True)
root.configure(bg='#23314A')
root.mainloop()