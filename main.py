import tkinter
import pyautogui


window = tkinter.Tk()

computerWidth = window.winfo_screenwidth()
computerHeight = window.winfo_screenheight()
appWidth = 1200
appHeight = 700

window.geometry(f"{appWidth}x{appHeight}+{int((computerWidth/2)-(appWidth/2))}+{int((computerHeight/2-(appHeight/2)))}") # center window to make it pretty :33
window.title("CONGRATATION!!!")


window.mainloop()
