from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI=Tk()
GUI.title('"ตารางเรียนลูก"')
GUI.geometry('500x500')

L1 = Label(GUI,text='ตารางเรียนลูก',font=('Arial Black',30),fg='blue')
L1.place(x=80,y=30)
###################
def Button1():
    text='วิทยาศาสตร์,คณิตศาตร์,ภาษาอังกฤษ,ภาษาจีน,สังคมศึกษา,ภาษาไทย'
    messagebox.showinfo('Monday',text)
    
FB1=Frame(GUI)
FB1.place(x=100,y=100)
B1=ttk.Button(FB1,text='Monday',command=Button1)
B1.pack(ipadx=50,ipady=20)
###################
def Button2():
    text='ภาษาอังกฤษ,ลูกเสือ,คณิตศาสตร์,ภาษาไทย,ดนตรี'
    messagebox.showinfo('Tueday',text)
    
FB2=Frame(GUI)
FB2.place(x=100,y=180)
B2=ttk.Button(FB2,text='Tueday',command=Button2)
B2.pack(ipadx=50,ipady=20)
###################
def Button3():
    text='ศิลปะ,คณิตศาสตร์,วิทยาศาสตร์,ภาษาไทย,ชมรม'
    messagebox.showinfo('Wednesday',text)
    
FB3=Frame(GUI)
FB3.place(x=100,y=260)
B3=ttk.Button(FB3,text='Wednesday',command=Button3)
B3.pack(ipadx=50,ipady=20)
###################
def Button4():
    text='ภาษาไทย,ประวัติศาสตร์,คณิตศาสตร์,สังคมศึกษา,ภาษาอังกฤษ'
    messagebox.showinfo('Thursday',text)
    
FB4=Frame(GUI)
FB4.place(x=100,y=340)
B4=ttk.Button(FB4,text='Thursday',command=Button4)
B4.pack(ipadx=50,ipady=20)
###################
def Button5():
    text='พลศึกษา,ภาษาไทย,คณิตศาสตร์,คอมพิวเตอร์,กอท.,เสริม'
    messagebox.showinfo('Friday',text)
    
FB5=Frame(GUI)
FB5.place(x=100,y=420)
B5=ttk.Button(FB5,text='Friday',command=Button5)
B5.pack(ipadx=50,ipady=20)
###################
GUI.mainloop()
