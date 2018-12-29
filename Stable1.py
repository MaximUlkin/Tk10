from tkinter.ttk import *
from tkinter import *
from random import *

import time
import os


#functions
def vt():
	print(v.get())

def addStudent():

	def addproceed():
		s.append(Student(fname_e.get(),lname_e.get(),age_e.get(),grade_e.get(),course_e.get()))
		newlen = len(s)-1
		rb.append(Radiobutton(main_Frame1,text=s[newlen].fullname(),
			indicatoron = 0,variable=v,value=newlen,font=("arial",9,"bold")))
		rb[newlen].pack(padx=6,pady=6)
		addsuccess()

	def addsuccess():
		addPage.destroy()
		success = Tk()
		success.title("Success")
		suclb1 = Label(success,
		text="Student Added Successfully",
		height=4,width=30,font=("arial",10,"bold"),fg="green")
		suclb1.pack()
		success.after(750,success.destroy)

	addPage = Tk()
	addPage.title("Add student")
	statlb1 = Label(addPage,
		text="To add a new student,\nplease fill in the following boxes :",
		height=4,width=30,font=("arial",11,"bold"))
	statlb1.grid(columnspan=2)
	#
	addFrame1 = Frame(addPage)
	addFrame1.grid(column=0,row=1)
	addFrame2 = Frame(addPage)
	addFrame2.grid(column=1,row=1)
	#
	fname_lb = Label(addFrame1,text="First name : ")
	fname_lb.grid(sticky=W)
	fname_e = Entry(addFrame2)
	fname_e.grid(sticky=W)
	#
	lname_lb = Label(addFrame1,text="Last name : ")
	lname_lb.grid(sticky=W)
	lname_e = Entry(addFrame2)
	lname_e.grid(sticky=W)
	#
	age_lb = Label(addFrame1,text="Age : ")
	age_lb.grid(sticky=W)
	age_e = Entry(addFrame2)
	age_e.grid(sticky=W)
	#
	grade_lb = Label(addFrame1,text="Grade : ")
	grade_lb.grid(sticky=W)
	grade_e = Entry(addFrame2)
	grade_e.grid(sticky=W)
	#
	course_lb = Label(addFrame1,text="Course : ")
	course_lb.grid(sticky=W)
	course_e = Entry(addFrame2)
	course_e.grid(sticky=W)
	#
	addFrame3 = Frame(addPage)
	addFrame3.grid(column=0,row=2,padx=10,pady=10)
	addFrame4 = Frame(addPage)
	addFrame4.grid(column=1,row=2,padx=10,pady=10)
	addbtn1 = Button(addFrame3,text="Cancel",font=("system",6)
		,height=1,width=6,command=addPage.destroy)
	addbtn1.grid(sticky=W)
	addbtn2 = Button(addFrame4,text="Proceed",font=("system",6)
		,height=1,width=6,fg="green",command=addproceed)
	addbtn2.grid(sticky=E)

def delStudent():
	def delproceed():
		notfound=True
		nonames=True
		for i in range(len(s)):
			if len(s)>=1:
				nonames=False
				if fname_e.get() == s[i].first and lname_e.get() == s[i].last:
					if len(s)==1:
						rb[0].destroy()
						rb.clear()
						s.clear()
						notfound=False
						delsuccess()
						break
					else:
						for x in range(i+1,len(s)):
							rb[x].config(value=x-1)
						rb[i].destroy()
						del s[i]
						print(s)
						notfound=False
						delsuccess()
						break
						break
		if notfound:
			if nonames:
				print("No names available to delete")
			else:
				print("Name not found")
				
		
	def delsuccess():
		delPage.destroy()
		delsuccessPage = Tk()
		delsuccessPage.title("Success")
		delsuclb1 = Label(delsuccessPage,text="Student has been removed successfully",height=4,width=35,font=("arial",11,"bold"),fg="green")
		delsuclb1.pack()
		delsuccessPage.after(750,delsuccessPage.destroy)
		
		

	delPage = Tk()
	delPage.title("Delete Student")
	statlb1 = Label(delPage,
		text="To delete a student,\n please enter his/her full name :",
		height=4,width=30,font=("arial",11,"bold"))
	statlb1.grid(columnspan=2)
	#
	delFrame1 = Frame(delPage)
	delFrame1.grid(column=0,row=1,padx=15,pady=15)
	delFrame2 = Frame(delPage)
	delFrame2.grid(column=1,row=1,padx=15,pady=15)
	#
	fname_lb = Label(delFrame1,text="First Name :")
	fname_lb.grid(sticky=W)
	fname_e = Entry(delFrame2)
	fname_e.grid(sticky=W)
	#
	lname_lb = Label(delFrame1,text="Last Name :")
	lname_lb.grid(sticky=W)
	lname_e = Entry(delFrame2)
	lname_e.grid(sticky=W)
	#
	delFrame3 = Frame(delPage)
	delFrame3.grid(column=0,row=2,padx=10,pady=10)
	delFrame4 = Frame(delPage)
	delFrame4.grid(column=1,row=2,padx=10,pady=10)
	delbtn1 = Button(delFrame3,text="Cancel",font=("system",6)
		,height=1,width=6,command=delPage.destroy)
	delbtn1.grid(sticky=W)
	delbtn2 = Button(delFrame4,text="Proceed",font=("system",6)
		,height=1,width=6,fg="green",command=delproceed)
	delbtn2.grid(sticky=E)

def delallStudent():

	def login(e,p):
		usr = "1234"
		pword = "1234"
		if e == (usr) and p == (pword):
			delallsuccess()
		else:
			print("wrong info")

	def delallsuccess():

		def finaldel():
			popsuc.destroy()
			s.clear()
			success = Tk()
			success.title("Success")
			successlb1 = Label(success,text="All names removed successfully",
				height=4,width=40,font=("arial",11,"bold"),
				fg="green")
			successlb1.grid(padx=20,pady=20)
			for i in range(len(rb)):
				rb[i].destroy()
			rb.clear()

		if len(s)==0:
			print("No names available to delete")
		else:
			delallPage.destroy()
			popsuc = Tk()
			popsuc.title("Delete Names")
			poplb1 = Label(popsuc,
			text="Login Success",
			height=4,width=40,font=("arial",9,"bold"),fg="white",bg="green")
			poplb1.grid(columnspan=2)
			poplb2 = Label(popsuc,
			text="Do you really want to delete all names?",
			height=4,width=30,font=("arial",11,"bold"))
			poplb2.grid(columnspan=2)
			popframe1 = Frame(popsuc)
			popframe1.grid(column=0,row=3,padx=10,pady=10)
			popframe2 = Frame(popsuc)
			popframe2.grid(column=1,row=3,padx=10,pady=10)
			popbtn1 = Button(popframe1,text="No",font=("system",6)
			,height=1,width=6,command=popsuc.destroy)
			popbtn1.grid(sticky=W)
			popbtn2 = Button(popframe2,text="Yes",font=("system",6)
			,height=1,width=6,fg="green",command=finaldel)
			popbtn2.grid(sticky=E)


		
		
	global delallPage
	delallPage = Tk()
	delallPage.title("Delete Multiple")
	#
	statlb1 = Label(delallPage,
		text="Admin Login to delete all students :",
		height=4,width=30,fg="white",bg="#66ff33",font=("arial",11))
	statlb1.grid(columnspan=2)
	#
	delallFrame1 = Frame(delallPage)
	delallFrame1.grid(column=0,row=1,padx=15,pady=15)
	delallFrame2 = Frame(delallPage)
	delallFrame2.grid(column=1,row=1,padx=15,pady=15)
	#
	user_lb = Label(delallFrame1,text="Username :")
	user_lb.grid(sticky=W)
	user_e = Entry(delallFrame2)
	user_e.grid(sticky=W)
	#
	pass_lb = Label(delallFrame1,text="Password :")
	pass_lb.grid(sticky=W)
	pass_e = Entry(delallFrame2)
	pass_e.grid(sticky=W)
	#
	delallFrame3 = Frame(delallPage)
	delallFrame3.grid(column=0,row=2,padx=10,pady=10)
	delallFrame4 = Frame(delallPage)
	delallFrame4.grid(column=1,row=2,padx=10,pady=10)
	delallbtn1 = Button(delallFrame3,text="Cancel",font=("system",6)
		,height=1,width=6,command=delallPage.destroy)
	delallbtn1.grid(sticky=W)
	delallbtn2 = Button(delallFrame4,text="Login",font=("system",6)
		,height=1,width=6,fg="green",command = lambda : login(user_e.get(),pass_e.get()))
	delallbtn2.grid(sticky=E)

def editName():
	def editproceed():
		print(var.get())

	editPage = Tk()
	editPage.title("Name Manager")
	#
	statlb1 = Label(editPage,
		text="Please make sure to\nselect the right name",
		height=4,width=30,font=("arial",11,"bold"))
	statlb1.grid(columnspan=2)
	#
	editFrame1 = Frame(editPage)
	editFrame1.grid(column=0,row=1,padx=15,pady=15)
	editFrame2 = Frame(editPage)
	editFrame2.grid(column=1,row=1,padx=15,pady=15)
	#
	edit_lb = Label(editFrame1,text="Select Full Name :")
	edit_lb.grid(sticky=W)
	#
	var = StringVar()

	# var.set(s[v.get()].fullname())
	edit_dd = ttk.OptionMenu(editFrame2,var,*fullname_list)
	# edit_ddconfigure(font=("arial",10),width=15)
	edit_dd.grid()
	#
	editFrame3 = Frame(editPage)
	editFrame3.grid(column=0,row=2,padx=10,pady=10)
	editFrame4 = Frame(editPage)
	editFrame4.grid(column=1,row=2,padx=10,pady=10)
	#
	editbtn1 = Button(editFrame3,text="Cancel",font=("system",6)
		,height=1,width=6,command=editPage.destroy)
	editbtn1.grid(sticky=W)
	editbtn2 = Button(editFrame4,text="Proceed",font=("system",6)
		,height=1,width=6,fg="green",command=editproceed)
	editbtn2.grid(sticky=E)

#class
class Student:

	def __init__(self,first,last,age,grade,course):
		self.first=first
		self.last=last
		self.age=age
		self.grade=grade
		self.course=course

	def fullname(self):
		return '{} {}'.format(self.first,self.last)


s=[]
s.append(Student("Maxim","Ulkin",15,10,"Programming"))



root = Tk()
root.title("Student Terminal")


#Menus
mastermenu = Menu(root)
root.config(menu=mastermenu)

namemenu = Menu(mastermenu,tearoff=False)
agemenu = Menu(mastermenu,tearoff=False)
grademenu = Menu(mastermenu,tearoff=False)
coursemenu = Menu(mastermenu,tearoff=False)
settingsmenu = Menu(mastermenu,tearoff=False)

mastermenu.add_cascade(label="Student",menu=namemenu)
namemenu.add_command(label="Add student",command=addStudent)
namemenu.add_command(label="Delete student",command=delStudent)
namemenu.add_command(label="Delete all",command=delallStudent)
namemenu.add_separator()
namemenu.add_command(label="Edit name",command=editName)

mastermenu.add_cascade(label="Age",menu=agemenu)
agemenu.add_command(label="Edit age")

mastermenu.add_cascade(label="Grade",menu=grademenu)
grademenu.add_command(label="Edit grade")

mastermenu.add_cascade(label="Course",menu=coursemenu)
coursemenu.add_command(label="View current courses")
coursemenu.add_separator()
coursemenu.add_command(label="Add course")
coursemenu.add_command(label="Course Manager")

mastermenu.add_cascade(label="Settings",menu=settingsmenu)
settingsmenu.add_command(label="Background Color")


#Labels
mainlb1 = Label(root,text="Welcome to the Student Terminal",
	width=40,height=4,font=("times",14,"bold"))
mainlb1.pack()
mainlb2 = Label(root,text="Please select a name to get started :",
	height=2,font=("times",13))
mainlb2.pack()
#Frame_1
main_Frame1 = Frame(root,relief=RIDGE,bd=4,padx=20,pady=20,bg="#FFB355")
main_Frame1.pack()

v = IntVar()
v.set(0)

rb=[]
fullname_list=[]
for i in range(len(s)):
	rb.append(Radiobutton(main_Frame1,text=s[i].fullname(),
		indicatoron = 0,variable=v,value=i,font=("arial",9,"bold")))
	fullname_list.append(s[i].fullname())
	rb[i].pack(padx=6,pady=6)






#Frame_2
main_Frame2 = Frame(root)
main_Frame2.pack()


#buttons
mainbtn1 = Button(root,text="Quit",font=("system",9,"bold")
	,fg="red",height=2,width=7,command=root.destroy)
mainbtn1.pack(side="left",padx=30,pady=10)
mainbtn2 = Button(root,text="Info",font=("system",9,"bold"),
	fg="green",height=2,width=7)
mainbtn2.pack(side="right",padx=30,pady=10)
testbtn = Button(root,text="Check V",command=vt)
testbtn.pack()





root.mainloop()