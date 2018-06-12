from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title("ttk GUI")
win.geometry('450x300')

label0=Label(win, text="ms").place(x=200, y= 50)
label1=Label(win, text="ms").place(x=200, y= 100)
label2=Label(win, text="ms").place(x=200, y= 150)

Open_delay_time= StringVar()
Open_delay_time.set('100')
OpenDelayTime = Entry(win, textvariable=Open_delay_time)
OpenDelayTime.place(x=50, y= 50)

Close_delay_time= StringVar()
Close_delay_time.set('200')
CloseDelayTime = Entry(win, textvariable=Close_delay_time)
CloseDelayTime.place(x=50, y= 100)

Third_delay_time= StringVar()
Third_delay_time.set('300')
ThirdDelayTime = Entry(win, textvariable=Third_delay_time)
ThirdDelayTime.place(x=50, y= 150)




button0=Button(win, text="OPEN",command=OpenStart)
button0.place(x=250, y= 50)
button1=Button(win, text="CLOSE").place(x=250, y= 100)
button2=Button(win, text="3rd.POSITION").place(x=250, y= 150)



def OpenStart():

	print("Start Opening !!!!1 ")






win.mainloop()