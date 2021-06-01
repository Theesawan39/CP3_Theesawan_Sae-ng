from tkinter import *

def sayHelloWorld():
   print("william hi")

MainWindow = Tk()
button = Button(MainWindow,text = "Click me yay1",command = sayHelloWorld).grid(row=0,column=1)
button2 = Button(MainWindow,text = "Click me yay2",command = sayHelloWorld).grid(row=1,column=1)
button3 = Button(MainWindow,text = "Click me yay3",command = sayHelloWorld).grid(row=0,column=2)
MainWindow.mainloop()

# mainWindow created for program working and do the actual window 
#from using make the function easier so we not gonna call out the first name of function anymore
#tk is tkinter the main thing that we using to manage the GUI
#all of the widgets will be created after Tk() 
