from tkinter import *
import math 

def LeftClickButton(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if ( result < 18.5):
        print("ผอมเกินไป")
    elif ( result >= 18.6 and labelResult <= 22.9):
        print("น้ำหนักเหมาะสม ปกติ")
    elif ( result >= 23.0 and labelResult <= 24.9):
        print("น้ำหนักเกิน")
    elif ( result >= 25.0  and labelResult <= 29.9):
        print("อ้วน")
    elif ( result >=30):
        print("อ้วนมาก")

MainWindow = Tk()
labelHeight = Label(MainWindow,text ="ส่วนสูง (cm)").grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text ="น้ำหนัก (kg)").grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

CalculateButton = Button(MainWindow,text ="คำนวณ")
CalculateButton.bind('<Button-1>',LeftClickButton)
CalculateButton.grid(row=2,column=0)


labelResult = Label(MainWindow,text ="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()

#Entry = textBox