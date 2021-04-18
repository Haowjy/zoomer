from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import backend

root = Tk()

def goToZoom(link):
    print("TODO: went to zoom..."+str(link)+"...")

class ZoomClass():

    def __init__(self, title, time, meeting_id, link):
         self.title = title
         self.time = time
         self.meeting_id = meeting_id
         self.link = link

    def create_frame(self, master=None):
        entireFrame = Frame(master=master,bg="#2D8CFE")
        entireFrame.bind("<Button-1>", lambda e : goToZoom(link=self.link))

        # buttonBackground = Image.open("dark_zoom_rectangle.png")
        # sized = buttonBackground.resize((int(buttonBackground.size[0]*0.10), int(buttonBackground.size[1]*0.10)))
        # photoImage = ImageTk.PhotoImage(sized)
        # label1 = Label(image=photoImage)
        # label1.pack()

        topFrame = Frame(master=entireFrame)
        labelTitle = Label(master=topFrame, text=self.title,font=('Arial', 25),  width=20, fg="#F4F4EB", bg="#2D8CFE")
        labelTitle.pack()
        labelTitle.bind("<Button-1>", lambda e : goToZoom(link=self.link))
        topFrame.pack()
        topFrame.bind("<Button-1>", lambda e : goToZoom(link=self.link))

        bottomFrame = Frame(master=entireFrame,borderwidth=3, bg="#2D8CFE")

        leftSide = Label(master=bottomFrame,text=self.meeting_id, fg="#F4F4EB", bg="#23314A")
        leftSide.grid(column=0, row=0,columnspan=9, sticky='w')
        leftSide.bind("<Button-1>", lambda e : goToZoom(link=self.link))
        centerLine = Label(master=bottomFrame, text="|", fg="#F4F4EB", bg="#2D8CFE")
        centerLine.grid(column=10,row=0, sticky='w')
        centerLine.bind("<Button-1>", lambda e : goToZoom(link=self.link))
        rightSide = Label(master=bottomFrame, text=self.time, fg="#F4F4EB", bg="#2D8CFE")
        rightSide.grid(column=11,row=0,columnspan=9, sticky='w')
        rightSide.bind("<Button-1>", lambda e : goToZoom(link=self.link))
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
        bottomFrame.bind("<Button-1>", lambda e : goToZoom(link=self.link))

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

def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=400, height=600)


root.geometry("400x600")
root.resizable(False, False)
root.configure(bg='#23314A')

myframe=Frame(root,width=400,height=600, bg='#23314A')
myframe.pack()

canvas=Canvas(myframe, width=400, bg='#23314A')
# canvas.bind('<MouseWheel>',lambda event:print(event))

frame=Frame(canvas, width=400, bg='#23314A')
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

# appFrame = Frame(width=400, height=600, bg='#23314A')

emptyFrame = Frame(frame, height=10,bg='#23314A')
emptyFrame.pack()


titleFrame = Frame(frame, width=400, bg='#23314A')
image1 = Image.open("zoomer_icon128.png")
image1 = image1.resize((int(image1.size[0]*.35), int(image1.size[1]*.35)))
test = ImageTk.PhotoImage(image1)

label1 = Label(titleFrame,image=test, bg="#23314A")
label1.image = test
label1.grid(column=0, row=0)

label2 = Label(titleFrame, text="Zoomer", font=('Arial', 25), bg="#23314A", fg="white")
label2.grid(column=1,row=0)
titleFrame.pack()

emptyFrame = Frame(frame, height=10,bg='#23314A')
emptyFrame.pack()

for i in range(10):
    zoomClass = ZoomClass("Title of Cal %i"%i, "April some some\nsome thing er", "999 9999 9999", "https://weewf%i"%i)
    zoomFrame = zoomClass.create_frame(frame)
    zoomFrame.pack(padx=50,pady=5)


# appFrame.pack()

# canvas = Canvas(root, height=0, width=400, bg='#23314A', border=0)
# canvas.pack()

root.mainloop()