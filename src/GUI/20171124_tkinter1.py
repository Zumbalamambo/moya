import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from PIL import Image

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
        
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):               
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
        tk.Frame.__init__(self, parent, bg='black')
                         
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im = Image.open("Moya_UI-01.png").resize((800,400))
        canvas.image = ImageTk.PhotoImage(im)        
        tk.Label(canvas, image = canvas.image, bg='white').grid(row=0, column=0)
                
        buttonImage = Image.open("Language.png").resize((80,80))
        self.buttonPhoto = ImageTk.PhotoImage(buttonImage) 
        buttonImage2 = Image.open("Quiz.png").resize((80,80))
        self.buttonPhoto2 = ImageTk.PhotoImage(buttonImage2)
        

        button11 = tk.Button(self,image=self.buttonPhoto,compound='center',bg='white',
                            command=lambda: controller.show_frame(PageOne))        
        button11.grid(row = 380, column =775)        
        button12 = tk.Button(self,image=self.buttonPhoto2,compound='center',bg='white',
                             command=lambda: controller.show_frame(PageTwo))
        button12.grid(row = 380, column = 785)       
        
class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="language", font=LARGE_FONT)
        label.grid(row=0, column=0)    
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im2 = Image.open("Moya_UI-06.png").resize((800,400))
        canvas.image2 = ImageTk.PhotoImage(im2)        
        tk.Label(canvas, image = canvas.image2, bg='white').grid(row=0, column=0)
        
        buttonImage22 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto22 = ImageTk.PhotoImage(buttonImage22)
        
        buttonImage23 = Image.open("Save.png").resize((80,80))
        self.buttonPhoto23 = ImageTk.PhotoImage(buttonImage23)

        buttonImage24 = Image.open("Quiz.png").resize((80,80))
        self.buttonPhoto24 = ImageTk.PhotoImage(buttonImage24)
        
        button21 = tk.Button(self,image=self.buttonPhoto22, compound='center',bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button21.grid(row=380, column=0)
        button22 = tk.Button(self, image=self.buttonPhoto23, compound='center',bg='white',
                            command=lambda: controller.show_frame(PageOne))
        button22.grid(row=380, column=775)
        button23 = tk.Button(self, image=self.buttonPhoto24, compound='center',bg='white',
                            command=lambda: controller.show_frame(PageTwo))
        button23.grid(row=380, column=785)

#        button24 = ttk.Button(self, text="Quiz",
#                            command=lambda: controller.show_frame(PageOne))
#        button24.grid(row=200, column=100)
#
#        button25 = ttk.Button(self, text="Quiz",
#                            command=lambda: controller.show_frame(PageOne))
#        button25.grid(row=200, column=300)
#
#        button26 = ttk.Button(self, text="Quiz",
#                            command=lambda: controller.show_frame(PageOne))
#        button26.grid(row=200, column=500)
#
#        button27 = ttk.Button(self, text="Quiz",
#                            command=lambda: controller.show_frame(PageOne))
#        button27.grid(row=200, column=700)        


class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
#        label = tk.Label(self, text="Quiz", font=LARGE_FONT)
#        label.grid(row=0, column=0)    
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im3 = Image.open("Moya_UI-02.png").resize((800,400))
        canvas.image3 = ImageTk.PhotoImage(im3)        
        tk.Label(canvas, image = canvas.image3, bg='white').grid(row=0, column=0)
        
        buttonImage = Image.open("Start.png").resize((220,220))
        self.buttonPhoto = ImageTk.PhotoImage(buttonImage)
        buttonImage22= Image.open("Home.png").resize((40,40))
        self.buttonPhoto22 = ImageTk.PhotoImage(buttonImage22)

        
        button32 = tk.Button(self,image=self.buttonPhoto, compound='center', bg='white',
                            command=lambda: controller.show_frame(PageThree))
        button32.grid(row=270, column=370)
        
        button32 = tk.Button(self,image=self.buttonPhoto22, compound='center', bg='white',
                            command=lambda: controller.show_frame(PageThree))
        button32.grid(row=300, column=25)
#        
#        button33 = ttk.Button(self, text="PageThree",
#                            command=lambda: controller.show_frame(PageThree))
#        button33.grid(row=370, column=775)

class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("Moya_UI-05.png").resize((800,400))
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
        
        im5 = Image.open("banana.jpg").resize((350,250))
        canvas.image5 = ImageTk.PhotoImage(im5)        
        label = tk.Label(self, image=canvas.image5, font=LARGE_FONT)
        label.grid(row=300, column=450)    

        buttonImage24 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto24 = ImageTk.PhotoImage(buttonImage24)
        button32 = tk.Button(self, image =  self.buttonPhoto24,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button32.grid(row=345, column=40)
        button33 = tk.Button(self, text="정답확인",
                            command=lambda: controller.show_frame(PageFour))
        button33.grid(row=350, column=700)
        

class PageFour(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("Moya_UI-04.png").resize((800,400))
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
#        label = tk.Label(self, text="PageThree", font=LARGE_FONT)
#        label.grid(row=100, column=400)    
        
        
        
        buttonImage41 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto41 = ImageTk.PhotoImage(buttonImage41)
        buttonImage42 = Image.open("Next.png").resize((80,80))
        self.buttonPhoto42 = ImageTk.PhotoImage(buttonImage42)
        
        
        button32 = tk.Button(self, image =  self.buttonPhoto41,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button32.grid(row=380, column=30)
        button33 = tk.Button(self, image =  self.buttonPhoto42,compound='center', bg='white',
                            command=lambda: controller.show_frame(PageTwo))
        button33.grid(row=380, column=760)
        
        
app = SeaofBTCapp()
app.mainloop()
        