#!/usr/bin/env python

import Tkinter as tk
from PIL import ImageTk
from PIL import Image
import rospy
from std_msgs.msg import String

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
        
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageRemote, PageTelephone, PageShoe, PageGlasses, PageVase, PageApple, PageTrump):               
            frame = F(container, self)       
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")   

        self.show_frame(StartPage)

        def callback(data):
            object_name = data.data
            if object_name == "trump":
                self.show_frame(PageTrump)
            elif object_name == "apple":
                self.show_frame(PageApple)
            elif object_name == "flower vase":
                self.show_frame(PageVase)
            elif object_name == "remote control":
                self.show_frame(PageRemote)
            elif object_name == "shoes":
                self.show_frame(PageShoe)
            elif object_name == "glasses":
                self.show_frame(PageGlasses)
            else:
                self.show_frame(PageTelephone)

        def receive_data():
            rospy.init_node('receive_data', anonymous=True)
            rospy.Subscriber('/classify_image', String, callback)


        receive_data()

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
                            command=lambda: controller.show_frame(PageThree), bd = 0)
        button32.grid(row=270, column=370)
        
        button33 = tk.Button(self,image=self.buttonPhoto22, compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage), bd=0,)
        button33.grid(row=300, column=25)
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
        label.grid(row=340, column=450)    

        buttonImage24 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto24 = ImageTk.PhotoImage(buttonImage24)
        buttonImage25 = Image.open("Check.png").resize((80,80))
        self.buttonPhoto25 = ImageTk.PhotoImage(buttonImage25)
        button32 = tk.Button(self, image =  self.buttonPhoto24,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button32.grid(row=345, column=40)
        button33 = tk.Button(self, image =  self.buttonPhoto25,compound='center', bg='white',
                            command=lambda: controller.show_frame(PageFour))
        button33.grid(row=345, column=750)
        

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



class PageRemote(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("../object_detection/testimages/testimages/remote control/remote_005.jpg")
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
        # label = tk.Label(self, text="PageFive", font=LARGE_FONT)
        # label.grid(row=200, column=400)

        buttonImage414 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto414 = ImageTk.PhotoImage(buttonImage414)
        button323 = tk.Button(self, image =  self.buttonPhoto414,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button323.grid(row=380, column=30)



class PageTelephone(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("../object_detection/testimages/testimages/telephone/telephone_001.jpg")
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
        # label = tk.Label(self, text="PageSix", font=LARGE_FONT)
        # label.grid(row=200, column=400)

        buttonImage424 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto424 = ImageTk.PhotoImage(buttonImage424)
        button324 = tk.Button(self, image =  self.buttonPhoto424,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button324.grid(row=380, column=30)

class PageShoe(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("../object_detection/testimages/testimages/shoes/shoes_001.jpg")
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
        # label = tk.Label(self, text="PageSix", font=LARGE_FONT)
        # label.grid(row=200, column=400)

        buttonImage424 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto424 = ImageTk.PhotoImage(buttonImage424)
        button324 = tk.Button(self, image =  self.buttonPhoto424,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button324.grid(row=380, column=30)



class PageGlasses(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("../object_detection/testimages/testimages/glasses/2Q==..jpg")
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
        # label = tk.Label(self, text="PageSix", font=LARGE_FONT)
        # label.grid(row=200, column=400)

        buttonImage424 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto424 = ImageTk.PhotoImage(buttonImage424)
        button324 = tk.Button(self, image =  self.buttonPhoto424,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button324.grid(row=380, column=30)

class PageVase(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("../object_detection/testimages/testimages/flower vase/pic2_005.jpg")
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
        # label = tk.Label(self, text="PageSix", font=LARGE_FONT)
        # label.grid(row=200, column=400)

        buttonImage424 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto424 = ImageTk.PhotoImage(buttonImage424)
        button324 = tk.Button(self, image =  self.buttonPhoto424,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button324.grid(row=380, column=30)

class PageApple(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("../object_detection/testimages/testimages/apple/apple1.jpg")
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
        # label = tk.Label(self, text="PageSix", font=LARGE_FONT)
        # label.grid(row=200, column=400)

        buttonImage424 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto424 = ImageTk.PhotoImage(buttonImage424)
        button324 = tk.Button(self, image =  self.buttonPhoto424,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button324.grid(row=380, column=30)

class PageTrump(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        
        canvas = tk.Canvas(self, width=800, height=400)
        canvas.grid(row=0, column=0, columnspan=800, rowspan=400)
        im4 = Image.open("../object_detection/testimages/testimages/trump/pic_001.jpg")
        canvas.image4 = ImageTk.PhotoImage(im4)        
        tk.Label(canvas, image = canvas.image4, bg='white').grid(row=0, column=0)
        # label = tk.Label(self, text="PageSix", font=LARGE_FONT)
        # label.grid(row=200, column=400)

        buttonImage424 = Image.open("Home.png").resize((40,40))
        self.buttonPhoto424 = ImageTk.PhotoImage(buttonImage424)
        button324 = tk.Button(self, image =  self.buttonPhoto424,compound='center', bg='white',
                            command=lambda: controller.show_frame(StartPage))
        button324.grid(row=380, column=30)


if __name__=='__main__':
    app = SeaofBTCapp()
    app.mainloop()
        
