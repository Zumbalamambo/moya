import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

LARGE_FONT= ("Verdana", 12)



class SeaofBTCapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Test file")


        container = tk.Frame(self)        
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)        
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):               
            frame = F(container, self)       
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")   

        self.show_frame(StartPage)

    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
        


def qf(param):
    print(param)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")
        label = tk.Label(self, text="MoYa on!", font=LARGE_FONT,background="white")
        label.grid(row=0, column=18)
        
        canvas = tk.Canvas(self, width=600, height=400)
        canvas.grid(row=1, column=0, columnspan=30)
        im = Image.open("eyes.gif")
        canvas.image = ImageTk.PhotoImage(im)        
        tk.Label(canvas,image = canvas.image).grid(row=0, column=0)
        
        
        buttonImage = Image.open('eyes.gif').resize((60,60))
        self.buttonPhoto = ImageTk.PhotoImage(buttonImage) 

        button11 = tk.Button(self,image=self.buttonPhoto,text="Language",compound='center',
                            command=lambda: controller.show_frame(PageOne))
        
        button11.grid(row = 2, column = 27)
        
        button12 = tk.Button(self, text="Quiz",
                            command=lambda: controller.show_frame(PageTwo))
        button12.grid(row = 2, column = 28)       
        
class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="language", font=LARGE_FONT)
        label.pack(pady=10, padx=10)    

        button21 = ttk.Button(self, text="Back to MoYa",
                            command=lambda: controller.show_frame(StartPage))
        button21.pack()

class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="Quiz", font=LARGE_FONT)
        label.pack(pady=10, padx=10)    

        button32 = ttk.Button(self, text="Back to MoYa",
                            command=lambda: controller.show_frame(StartPage))
        button32.pack()




        
app = SeaofBTCapp()
app.mainloop()
        