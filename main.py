#! This is bad
import pyautogui
import time
from tkinter import *
import webbrowser
from PIL import Image, ImageTk

root=Tk()
computerWidth = root.winfo_screenwidth()
computerHeight = root.winfo_screenheight()
appWidth = 1200
appHeight = 800

def shift():
    x1,y1,x2,y2 = colourCanvas.bbox("marquee")
    if(x2<0 or y1<0):
        x1 = colourCanvas.winfo_width()
        y1 = colourCanvas.winfo_height()//2
        colourCanvas.coords("marquee",x1,y1)
    else:
        colourCanvas.move("marquee", -2, 0)
    colourCanvas.after(1000//fps,shift)

colors = ["red", "blue"]
def updateBackgroundColor(index=0):
    colourCanvas.config(background=colors[index])
    root.after(10, updateBackgroundColor, 1 - index)  


root.title('CONGRATATATION!!!')
root.geometry(f"{appWidth}x{appHeight}+{int((computerWidth/2)-(appWidth/2))}+{int((computerHeight/2-(appHeight/2)))}") # center window to make it pretty :33
root.configure(background="green")

colourCanvas=Canvas(root,bg='black')
colourCanvas.pack(fill=BOTH, expand=1)
text_var="thomas petkovic"
text=colourCanvas.create_text(0,-2000,text=text_var,font=('Comic Sans MS',40,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = colourCanvas.bbox("marquee")
width = x2-x1
height = y2-y1
colourCanvas['width']=width
colourCanvas['height']=height
fps=300

eatgif = ImageTk.PhotoImage(Image.open("eatgif.gif"))
picture = Label(root,image=eatgif,bg='Yellow')
picture.pack(side='bottom',fill='both',expand='yes')
shift()

updateBackgroundColor()

kevinJamesHot = PhotoImage(file="kevinJames.png",)
kevinJamesHotCanvas = colourCanvas.create_image(appWidth/2, appHeight/5, anchor=CENTER, image=kevinJamesHot)

def linkButtonFunction():
    webbrowser.open("https://canadacrimeindex.com/crime-severity-index?sort=population&min_population=0&province=")

openLinkButton = Button(root, text = "View Crime Statistics", bd = "20", command = linkButtonFunction) 
openLinkButton.pack(side = "left") 

def lockButtonFunction():
    pyautogui.confirm("ASK ABOUT THE LOCKS WHEN YOUR HOMELESS FOR YOUR HOUSE") 

openLinkButton = Button(root, text = "Lock", bd = "20", command = lockButtonFunction) 
openLinkButton.pack(side = "right") 

root.mainloop()