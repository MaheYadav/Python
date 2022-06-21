import sqlite3
con=sqlite3.connect("amr.db")
sq="select ename,sal,dsg from where eid=%d"
eno=int(input("Enter emp id:"))
cur=con.execute(sq  % eno)
recs=cur.fetchall()
if(len(recs)!=0):
	for rec in recs:
		print("{}|t {}|t {}|t".format(rec[0],rec[1],rec[2]))
else:
	print("emp record does not exist")
