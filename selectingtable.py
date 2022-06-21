import sqlite3
con=sqlite3.connect("amr.db")
sq="select * from emp"
recs=con.execute(sq)
for rec in recs:
	print("________________")
	print("emp id:",rec[0])
	print("emp name:",rec[1])
	print("emp sal:",rec[2])
	print("emp dsg:",rec[3])
	print("________________")