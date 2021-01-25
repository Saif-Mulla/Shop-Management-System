from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import datetime

class shop:
	def Bill(self):
		bill = Tk()
		bill.title("Bill")
		bill.geometry("850x780")
		bill.configure(highlightbackground="black",highlightthickness=3,bg ="light grey")
		Label(bill,text="Bill",fg="blue",bg='light grey',font=("arial",20,"bold")).grid(row=0,column=1)
		Label(bill,text="",bg='light grey').grid(row=1,column=0)
		Label(bill,text="Phone Number",bg='light grey',font=("Helvetica",16,"bold")).grid(row=2,column=0)
		phone_entry=Entry(bill,width=30,font=("Helvetica",12))
		phone_entry.grid(row=2,column=1)
		Label(bill,text="",bg='light grey').grid(row=3,column=0)

		#Label(bill,text="Phone Number",bg='light grey',font=("Helvetica",16,"bold")).grid(row=4,column=0)
		#phone_entry=Entry(bill,width=30,font=("Helvetica",12))
		#phone_entry.grid(row=4,column=1)
		#Label(bill,text="",bg='light grey').grid(row=5,column=0)

		items_label=Label(bill,text="Items",bg="light grey",font=("Helvetica",16)).grid(row=4,column=0)
		price_label=Label(bill,text="Price",bg="light grey",font=("Helvetica",16)).grid(row=4,column=1)


		class one:
			def __init__(self):		
				self.r=5;self.total=0;self.I=[];self.P=[];self.c=0;self.i=0;self.price=[];self.items=[]
	
			def plus(self,event):
				items_entry=Entry(bill,width=25,font=("Helvetica",16))
				items_entry.grid(row=self.r,column=self.c)
				price_entry=Entry(bill,width=10,font=("Helvetica",16))
				price_entry.grid(row=self.r,column=self.c+1)
				self.price.append(price_entry)
				self.items.append(items_entry)
				self.r=self.r+1
				self.i=self.i+1
				Label(bill,text="",bg='light grey').grid(row=self.r,column=0)	
		
		
		a=one()

		plus_button=Button(bill,text="Add-Items",width=10,height=1,bg="yellow",font=("arial",14))
		plus_button.grid(row=4,column=2)
		plus_button.bind("<Button-1>",a.plus)
		
		def add():
			for x in range(a.i):
				a.I.append(a.items[x].get())
				a.P.append(a.price[x].get())
				a.total=int(a.total)+int(a.price[x].get())
			total_label = Label(bill,text=a.total,width=10,bg="light grey",fg="black",font=("arial",20,"bold")).grid(row=49,column=1)
			a.i=0
		
		
		Label(bill,text="",bg='light grey').grid(row=50,column=0)		
		Add=Button(bill,text="Total",command=add,width=10,height=1,bg="light green",fg="blue",font=("arial",14,"bold"))
		Add.grid(row=51,column=1)

		def store():
			I1=(((str(a.I).replace("'"," ")).replace("[","'")).replace("]","'"))
			P1=(((str(a.P).replace("'"," ")).replace("[","'")).replace("]","'"))
			mydb=mysql.connector.connect(host="localhost",user="root",passwd="saif123",database="shop")
			mycursor=mydb.cursor()
			dt=datetime.now()
			date=dt.strftime("%Y-%m-%d %H:%M:%S")
			print((phone_entry.get()),I1,P1,a.total,date,"0")
			mycursor.execute("create table if not exists bill_table(ID int primary key auto_increment,PhoneNumber varchar(20),Date_Time timestamp,Items longtext,price text,Total int,Status bool ,index pno_idx (PhoneNumber),foreign key(PhoneNumber) references Account_table(PhoneNumber))")
			sql="INSERT INTO bill_table(PhoneNumber,Date_Time,Items,price,Total,Status) VALUES (%s,%s,%s,%s,%s,0)"
			val=(phone_entry.get(),date,I1,P1,a.total)
				
			try:
				mycursor.execute(sql,val)
				mydb.commit()
				messagebox.showinfo("Message","Customer Bill Saved")
			except mysql.connector.Error:
				messagebox.showwarning("Error Message","Failed to Insert Enter Valid Phone Number")
			finally:
				bill.destroy()

		def pay():
			I1=(((str(a.I).replace("'"," ")).replace("[","'")).replace("]","'"))
			P1=(((str(a.P).replace("'"," ")).replace("[","'")).replace("]","'"))
			mydb=mysql.connector.connect(host="localhost",user="root",passwd="saif123",database="shop")
			mycursor=mydb.cursor()
			dt=datetime.now()
			date=dt.strftime("%Y-%m-%d %H:%M:%S")
			print((phone_entry.get()),I1,P1,a.total,date,"1")
			mycursor.execute("create table if not exists bill_table(ID int primary key auto_increment,PhoneNumber varchar(20),Date_Time timestamp,Items longtext,price text,Total int,Status bool ,index pno_idx (PhoneNumber),foreign key(PhoneNumber) references Account_table(PhoneNumber))")
			sql="INSERT INTO bill_table(PhoneNumber,Date_Time,Items,price,Total,Status) VALUES (%s,%s,%s,%s,%s,1)"
			val=(phone_entry.get(),date,I1,P1,a.total)
				
			try:
				mycursor.execute(sql,val)
				mydb.commit()
				messagebox.showinfo("Message","Taking print")
			except mysql.connector.Error:
				messagebox.showwarning("Error Message","Failed Please Enter a Valid Phone Number")
			finally:
				bill.destroy()


		d1_button = Button(bill,text="Later",command=store,width=15,height=1,bg="aqua",fg="red",font=("arial",16,"bold")).grid(row=51,column=0)
		d2_button = Button(bill,text="Pay",command=pay,width=15,height=1,bg="aqua",fg="red",font=("arial",16,"bold")).grid(row=51,column=2)

		bill.mainloop()

	def customer_details(self):
		from PIL import ImageTk,Image
		details = Tk()
		details.title("Customer Details")
		details.geometry("800x300")
		details.configure(bg ="light grey")
		#c_img = ImageTk(d_I)
		#c_label = Label(details,image=c_img)
		#c_label.grid(row=2,column=3)
		self.check_box=[]
		self.zz=0
		Label(details,text="Please Enter Customer Details",fg="dark Green",bg='light grey',font=("Monotype corsiva",26,"bold")).grid(row=0,column=2)
		Label(details,text="",bg='light grey').grid(row=1,column=0)
	
		d1=Label(details,text="Customer Phone Number",width=20,height=2,bg='light grey',font=("Helvetica",12,"bold")).grid(row=2,column=1)
		d1_entry=Entry(details,font=("Helvetica",14))
		d1_entry.grid(row=2,column=2)

		Label(details,text="",bg="light grey").grid(row=3,column=1)
		def Ok():
			z=d1_entry.get()

			rw=2
			cl=0
			ck=[]
			display=Tk()
			display.title("Customer Information")
			display.geometry("1500x600")
			display.configure(bg = "light grey")
			Label(display,text="Customer Information",width =18,height=2,bg='light grey',font=("Helvetica",16,"bold")).grid(row=0,column=3)
			Label(display,text="ID",width =6,bg="light grey",font=("Helvetica",12,"bold")).grid(row=1,column=0)
			Label(display,text="Phone Number",width =15,bg="light grey",font=("Helvetica",12,"bold")).grid(row=1,column=1)
			Label(display,text="Date Time",width =18,bg="light grey",font=("Helvetica",12,"bold")).grid(row=1,column=2)
			Label(display,text="Items",width =40,bg="light grey",font=("Helvetica",12,"bold")).grid(row=1,column=3)
			Label(display,text="Price",width =34,bg="light grey",font=("Helvetica",12,"bold")).grid(row=1,column=4)
			Label(display,text="Total",width =10,bg="light grey",font=("Helvetica",12,"bold")).grid(row=1,column=5)
			Label(display,text="Status",width =10,bg="light grey",font=("Helvetica",12,"bold")).grid(row=1,column=6)
			mydb=mysql.connector.connect(host="localhost",user="root",passwd="saif123",database="shop")
			mycursor=mydb.cursor()
			#mycursor.execute("select * from bill_table where PhoneNumber = 7066527364") 
			mycursor.execute("select * from bill_table where PhoneNumber = "+z)
			records=mycursor.fetchall()
			print("Records: ",records)
			for row in records:
				cnt=0
				print(z)
				Label(display,text=row[0],width =6,bg="light grey",font=("arial",12)).grid(row=rw,column=cl)
				Label(display,text=row[1],width =15,bg="light grey",font=("arial",12)).grid(row=rw,column=cl+1)
				Label(display,text=row[2],width =18,bg="light grey",font=("arial",12)).grid(row=rw,column=cl+2)
				Label(display,text=row[3],width =40,bg="light grey",font=("arial",12)).grid(row=rw,column=cl+3)
				Label(display,text=row[4],width =34,bg="light grey",font=("arial",12)).grid(row=rw,column=cl+4)
				Label(display,text=row[5],width =10,bg="light grey",font=("arial",12)).grid(row=rw,column=cl+5)
				if row[6]==0:
					Label(display,text="Not Paid",width =10,bg="light grey",font=("arial",12)).grid(row=rw,column=cl+6)
				elif row[6]==1:
					Label(display,text="Paid",width =10,bg="light grey",font=("arial",12)).grid(row=rw,column=cl+6)
				var=IntVar()
				# self.check_box[self.zz]=Checkbutton(display,bg="light grey",variable=var,onvalue = 1, offvalue = 0, height=2,width=6)
				# print(self.check_box[self.zz])
				# self.check_box[self.zz].grid(row=rw,column=cl+7)
				# zz+=1
				rw+=1
				cnt+=1
				Label(display,text="",bg='light grey').grid(row=46,column=0)

			Label(display,text="",bg='light grey').grid(row=48,column=0)
			Label(display,text="",bg='light grey').grid(row=49,column=0)

			def ttl():
					print("saif")
			
			def Print():
				messagebox.showinfo("Message","Taking Print")
				# display.destroy()
				# details.destroy()

			def del_acc():
				del_msg=messagebox.askyesno("Message","Are You Sure You Want To Delete")
				if del_msg==1:
					mycursor.execute("set sql_safe_updates=0")
					mycursor.execute("delete from bill_table where bill_table.PhoneNumber="+z)
					mycursor.execute("delete from Account_table where Account_table.PhoneNumber="+z)
					mycursor.execute("set sql_safe_updates=1")
					mydb.commit()
				elif del_msg==0:
					messagebox.showinfo("Message","Account Not Deleted")

				display.destroy()
				details.destroy()	
			
			disp_btn = Button(display,text="Print",command=Print,width=15,height=1,bg="Light green",fg="blue",font=("arial",12,"bold")).grid(row=51,column=5)
			tot_btn = Button(display,text="Total",command=ttl,width=15,height=1,bg="Light green",fg="blue",font=("arial",12,"bold")).grid(row=51,column=3)
			del_btn = Button(display,text="Delete Account",command=del_acc,width=15,height=1,bg="Light green",fg="blue",font=("arial",12,"bold")).grid(row=51,column=1)  
			display.mainloop()
		d_button = Button(details,text="Ok",command=Ok,width=15,height=2,bg="yellow",fg="red",font=("arial",13,"bold")).grid(row=4,column=2)  
		details.mainloop()

	def account(self):
		window=Tk()
		window.geometry("650x650")
		window.title("Create Account")
		#window.iconbitmap('C:\\Users\\Suhaqi\\Desktop\\New folder\\writing.png')
		window.configure(bg='light grey')

		#Create A Account
	
		Label(window,text="Please Enter Customer Details",bg="light grey",fg="purple",font=("Monotype corsiva",30,"bold")).pack()
		Label(window,text="",bg="light grey").pack()
		l1=Label(window,text="Customer Name",bg="light grey",font=("Helvetica",14,"bold"))
		l1.pack()

		l1_entry=Entry(window,width=40,font=("Helvetica",10))
		l1_entry.pack()

		Label(window,text="",bg="light grey").pack()

		l2=Label(window,text="Phone Number",bg="light grey",font=("Helvetica",14,"bold"))
		l2.pack()

		l2_entry=Entry(window,width=40,font=("Helvetica",10))
		l2_entry.pack()

		Label(window,text="",bg="light grey").pack()

		l3=Label(window,text="Address",bg="light grey",font=("Helvetica",14,"bold"))
		l3.pack()

		l3_entry=Text(window,width=35,height=5,font=("Helvetica",11))
		l3_entry.pack()

		Label(window,text="",bg="light grey").pack()

		def submit():
			mydb=mysql.connector.connect(host="localhost",user="root",passwd="saif123",database="shop")
			mycursor=mydb.cursor()
			mycursor.execute("create table if not exists Account_table(CustomerName varchar(20),PhoneNumber varchar(20) primary key,CustomerAddress text)")
			sql="INSERT INTO Account_table(CustomerName,PhoneNumber,CustomerAddress) VALUES (%s,%s,%s)"
			val=(l1_entry.get(),l2_entry.get(),l3_entry.get('1.0',END))
			mycursor.execute(sql,val)
			mydb.commit()
			messagebox.showinfo("Message",(mycursor.rowcount, " Record Inserted. "))
			window.destroy()


		Button(window,text="Submit",command=submit,width=15,height=2,bg="yellow",fg="red",font=("arial",12,"bold")).pack()
		window.mainloop()

S=shop()


def main_screen():
	main_screen=Tk()
	main_screen.geometry("750x450")
	main_screen.title("Main Screen")
	main_screen.iconbitmap('D:\\PythonProg\\Shop\\Picture\\writing.png')

	Label(main_screen,text="Main Menu",width=50,fg="blue",font=("Monotype corsiva",30,"bold")).pack()
	Label(main_screen,text="").pack()
	Label(main_screen,text="").pack()

	Button(main_screen,text="Create Account",command=S.account,width=50,height=3,bg="light green",font=("arial",12,"bold")).pack()
	Label(main_screen,text="").pack()

	Button(main_screen,text="Bill",command=S.Bill, width=50,height=3,bg="light green",font=("arial",12,"bold")).pack()
	Label(main_screen,text="").pack()
	
	Button(main_screen,text="Customer Details",command=S.customer_details,width=50,height=3,bg="light green",font=("arial",12,"bold")).pack()
	Label(main_screen,text="").pack()

	main_screen.mainloop()


welcome_screen=Tk()
welcome_screen.geometry("800x350")
welcome_screen.title("Welcome to Shop")
welcome_screen.configure(bg='light grey')

p1=PhotoImage(file='D:\\PythonProg\\Shop\\Picture\\store.png')
welcome_screen.iconphoto(False,p1)
 
Label(welcome_screen,text="Welcome to Shop",fg="red",bg='light grey',font=("Monotype corsiva",30,"bold")).grid(row=0,column=1)
Label(welcome_screen,text="",bg='light grey').grid(row=1,column=0)

w1=Label(welcome_screen,text="Password",width=20,height=2,bg='light grey',font=("Helvetica",12,"bold")).grid(row=2,column=0)
w1_entry=Entry(welcome_screen,show='*')
w1_entry.grid(row=2,column=1)

my_img = ImageTk.PhotoImage(Image.open("D:\\PythonProg\\Shop\\Picture\\s1.png"))
img_label = Label(image=my_img)
img_label.grid(row=2,column=3)

def msg():
    messagebox.showerror("Message Box","Incorrect Password")

def clicked():
	if w1_entry.get() == 'shop123':
		welcome_screen.destroy()
		mydb=mysql.connector.connect(host="localhost",user="root",passwd="saif123")
		mycursor=mydb.cursor()
		mycursor.execute("create database if not exists shop")
		main_screen()
	else:
		msg()
		w1_entry.delete(first=0,last=30)


b1=Button(welcome_screen,text="Go",command=clicked,width=15,height=2,bg="light green",fg="dark red",font=("arial",12,"bold")).grid(row=3,column=1)
welcome_screen.mainloop()
