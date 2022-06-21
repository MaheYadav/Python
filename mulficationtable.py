n=int(input("Enter  a multification table:"))
if (n<=0):
	print("{}is invalid input,enter positive:".format(n))
else:
	print("-"*50)
	print("mul table for:",n)
	print("-"*50)
	for i in range(1,11):
		print("\t\t{}*{}={}".format(n,i,n*i))
	else:
		print("-"*50)
		print("mul table generated:")
print("Thanks using for this app")
