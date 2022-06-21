class employee:
    def __init__(self):
        print("This is non parameterized constructor")
    def dispaly(self,name):
        print("Hello",name)
e=employee()
e.dispaly("Maheedar")
class student:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def display(self):
        print("Hlo i am principle Tell me ur name and number",self.name,self.number)
s=student("Suman",9700993858)
s.display()
av=getattr(s,"name")
a=getattr(s,"number")
print(av)
print(a)
re= delattr(s,'number',)
print(re)
class labour:
    name="Ramanaiah"
    land =20
    def display(self):
      print("Labour name:",self.name,"Labour land:",self.land)
l=labour()
l.display()
