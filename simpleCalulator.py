from tkinter import *
root=Tk()
root.title('Calculator')

'''my_label1 = Label(root,text="Hello World")
my_label1.pack()'''

def btn_click(number):
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current) + str(number))

def btn_clear():
	e.delete(0,END)

def btn_add():
	global first_number
	global operation
	operation="addition"
	first_number=float(e.get())
	e.delete(0,END)

def btn_Minus():
	global first_number
	global operation
	operation="minus"
	first_number=float(e.get())
	e.delete(0,END)

def btn_multy():
	global first_number
	global operation
	operation="multiply"
	first_number=float(e.get())
	e.delete(0,END)

def btn_divide():
	global first_number
	global operation
	operation="devision"
	first_number=float(e.get())
	e.delete(0,END)

def btn_equal():
	second_number=e.get()
	e.delete(0,END)
	if operation=="addition":
		e.insert(0, first_number + float(second_number))
	elif operation=="minus":
		e.insert(0, first_number - float(second_number))
	elif operation=="multiply":
		e.insert(0, first_number * float(second_number))
	elif operation=="devision":
		e.insert(0, first_number / float(second_number))


e= Entry(root,width=50)
e.grid(row=0,column=0,columnspan=4,pady=10,ipady=10)
#e.insert(0,0)

#Button define

button_0 = Button(root,text="0",padx=67,pady=20,command=lambda: btn_click(0))
button_1 = Button(root,text="1",padx=30,pady=20,command=lambda: btn_click(1))
button_2 = Button(root,text="2",padx=30,pady=20,command=lambda: btn_click(2))
button_3 = Button(root,text="3",padx=30,pady=20,command=lambda: btn_click(3))
button_4 = Button(root,text="4",padx=30,pady=20,command=lambda: btn_click(4))
button_5 = Button(root,text="5",padx=30,pady=20,command=lambda: btn_click(5))
button_6 = Button(root,text="6",padx=30,pady=20,command=lambda: btn_click(6))
button_7 = Button(root,text="7",padx=30,pady=20,command=lambda: btn_click(7))
button_8 = Button(root,text="8",padx=30,pady=20,command=lambda: btn_click(8))
button_9 = Button(root,text="9",padx=30,pady=20,command=lambda: btn_click(9))
button_Equal = Button(root,text="=",padx=33,pady=53,command=btn_equal)
button_Plus = Button(root,text="+",padx=67,pady=20,command=btn_add)
button_Minus = Button(root,text="-",padx=33,pady=20,command=btn_Minus)
button_Multy = Button(root,text="*",padx=30,pady=20,command=btn_multy)
button_Divide = Button(root,text="/",padx=31,pady=20,command=btn_divide)
button_Clear = Button(root,text="CE",padx=30,pady=53,command=btn_clear)

#Button Placed

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_Clear.grid(row=1,column=3,rowspan=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_Minus.grid(row=3,column=3)
button_0.grid(row=4,column=0,columnspan=2)
button_Divide.grid(row=4,column=2)
button_Equal.grid(row=4,column=3,rowspan=2)
button_Multy.grid(row=5,column=0)
button_Plus.grid(row=5,column=1,columnspan=2)

theame= IntVar()
#theame.set("0")
#theame.get()

def apply_theame(value):
	if value==0:
		button_0 = Button(root,text="0",padx=67,pady=20,command=lambda: btn_click(0))
		button_1 = Button(root,text="1",padx=30,pady=20,command=lambda: btn_click(1))
		button_2 = Button(root,text="2",padx=30,pady=20,command=lambda: btn_click(2))
		button_3 = Button(root,text="3",padx=30,pady=20,command=lambda: btn_click(3))
		button_4 = Button(root,text="4",padx=30,pady=20,command=lambda: btn_click(4))
		button_5 = Button(root,text="5",padx=30,pady=20,command=lambda: btn_click(5))
		button_6 = Button(root,text="6",padx=30,pady=20,command=lambda: btn_click(6))
		button_7 = Button(root,text="7",padx=30,pady=20,command=lambda: btn_click(7))
		button_8 = Button(root,text="8",padx=30,pady=20,command=lambda: btn_click(8))
		button_9 = Button(root,text="9",padx=30,pady=20,command=lambda: btn_click(9))
		button_Equal = Button(root,text="=",padx=33,pady=53,command=btn_equal)
		button_Plus = Button(root,text="+",padx=67,pady=20,command=btn_add)
		button_Minus = Button(root,text="-",padx=33,pady=20,command=btn_Minus)
		button_Multy = Button(root,text="*",padx=30,pady=20,command=btn_multy)
		button_Divide = Button(root,text="/",padx=31,pady=20,command=btn_divide)
		button_Clear = Button(root,text="CE",padx=30,pady=53,command=btn_clear)		
		root.configure(bg="white")

		button_7.grid(row=1,column=0)
		button_8.grid(row=1,column=1)
		button_9.grid(row=1,column=2)
		button_Clear.grid(row=1,column=3,rowspan=2)
		button_4.grid(row=2,column=0)
		button_5.grid(row=2,column=1)
		button_6.grid(row=2,column=2)
		button_1.grid(row=3,column=0)
		button_2.grid(row=3,column=1)
		button_3.grid(row=3,column=2)
		button_Minus.grid(row=3,column=3)
		button_0.grid(row=4,column=0,columnspan=2)
		button_Divide.grid(row=4,column=2)
		button_Equal.grid(row=4,column=3,rowspan=2)
		button_Multy.grid(row=5,column=0)
		button_Plus.grid(row=5,column=1,columnspan=2)
	elif value==1:
		button_0 = Button(root,text="0",padx=67,pady=20,command=lambda: btn_click(0),fg="white",bg="black")
		button_1 = Button(root,text="1",padx=30,pady=20,command=lambda: btn_click(1),fg="white",bg="black")
		button_2 = Button(root,text="2",padx=30,pady=20,command=lambda: btn_click(2),fg="white",bg="black")
		button_3 = Button(root,text="3",padx=30,pady=20,command=lambda: btn_click(3),fg="white",bg="black")
		button_4 = Button(root,text="4",padx=30,pady=20,command=lambda: btn_click(4),fg="white",bg="black")
		button_5 = Button(root,text="5",padx=30,pady=20,command=lambda: btn_click(5),fg="white",bg="black")
		button_6 = Button(root,text="6",padx=30,pady=20,command=lambda: btn_click(6),fg="white",bg="black")
		button_7 = Button(root,text="7",padx=30,pady=20,command=lambda: btn_click(7),fg="white",bg="black")
		button_8 = Button(root,text="8",padx=30,pady=20,command=lambda: btn_click(8),fg="white",bg="black")
		button_9 = Button(root,text="9",padx=30,pady=20,command=lambda: btn_click(9),fg="white",bg="black")
		button_Equal = Button(root,text="=",padx=33,pady=53,command=btn_equal,fg="white",bg="black")
		button_Plus = Button(root,text="+",padx=67,pady=20,command=btn_add,fg="white",bg="black")
		button_Minus = Button(root,text="-",padx=33,pady=20,command=btn_Minus,fg="white",bg="black")
		button_Multy = Button(root,text="*",padx=30,pady=20,command=btn_multy,fg="white",bg="black")
		button_Divide = Button(root,text="/",padx=31,pady=20,command=btn_divide,fg="white",bg="black")
		button_Clear = Button(root,text="CE",padx=30,pady=52,command=btn_clear,fg="white",bg="black")
		root.configure(bg="black")

		button_7.grid(row=1,column=0)
		button_8.grid(row=1,column=1)
		button_9.grid(row=1,column=2)
		button_Clear.grid(row=1,column=3,rowspan=2)
		button_4.grid(row=2,column=0)
		button_5.grid(row=2,column=1)
		button_6.grid(row=2,column=2)
		button_1.grid(row=3,column=0)
		button_2.grid(row=3,column=1)
		button_3.grid(row=3,column=2)
		button_Minus.grid(row=3,column=3)
		button_0.grid(row=4,column=0,columnspan=2)
		button_Divide.grid(row=4,column=2)
		button_Equal.grid(row=4,column=3,rowspan=2)
		button_Multy.grid(row=5,column=0)
		button_Plus.grid(row=5,column=1,columnspan=2)

theame_label=Label(root,text="Theame").grid(row=6,column=0)
Radiobutton(root,text="Light",variable=theame,value=0,command=lambda: apply_theame(theame.get())).grid(row=6,column=1,columnspan=2)
Radiobutton(root,text="Dark",variable=theame,value=1,command=lambda: apply_theame(theame.get())).grid(row=6,column=3)

#apply_btn = Button(root,text="Apply Selected Theame").grid(row=7,column=0,columnspan=4,command= lambda: apply_theame(theame.get()))

root.mainloop()