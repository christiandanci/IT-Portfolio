from tkinter import *   
myEvents = Tk()  
myEvents.geometry("500x300")
def SayHello():  
    print("Welcome to Windows Trial")
def Exit():
    print("Good Bye")
    myEvents.destroy()
b1 = Button(myEvents,text = "Click Me",command = SayHello)
b2 = Button(myEvents,text = "End",command = Exit)
b1.pack()
b2.pack()  
myEvents.mainloop()
