import sqlite3
con=sqlite3.connect("amr.db")
while True:
	print("----------")
	eno=int(input("Enter Emp Number:"))
	name=input("Enter Emp Name:")
	sal=float(input("Enter Emp sal:"))
	dsg=input("Enter Emp Designation:")
	iq="insert into Emp values(%d,'%s',%f,'%s')"
	con.execute(iq %(eno,name,sal,dsg))
	con.commit()
	print("-----------")
	print("record inserted")
	print("-----------")
	ch=input("do u want to insert another record(yes/no):")
	if((ch=="no")or(ch=="No")or(ch=="NO")or(ch=="nO")):
			break

	
 
	
