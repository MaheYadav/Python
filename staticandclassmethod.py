class employee:
    name="mahi"
    id=1
    @staticmethod
    def display1():
        print("Employee Name:",employee.name)
        print("Employee Id:",employee.id)
    @classmethod
    def display(cls):
        print("I am a class method")
        # print(type(cls))
    @classmethod
    def show(cls):
        print("i am robo")
        # print(type(cls))
    def show1(self):
        print("Program is over")
employee.display1()
employee.display()
employee.show()
e=employee()
e.show1()
