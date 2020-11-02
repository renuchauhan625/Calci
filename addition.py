from tkinter import *
root=Tk()
root.title("Addition")
root.geometry('500x300')

l1=Label(root,text="Enter first number")
l1.grid(row=0,column=0,padx=5,pady=10)
t1=Entry(root)
t1.grid(row=0,column=1)
l2=Label(root,text="Enter second number")
l2.grid(row=2,column=0,padx=6,pady=10)
t2=Entry(root)
t2.grid(row=2,column=1)
def Add():
    l3.config(text=int(t1.get())+int(t2.get()))

b1=Button(root,command=Add,text="Add")
b1.grid(row=4,column=1,sticky=W)
l3=Label(root,text="")
l3.grid(row=4,column=2)

root.mainloop()