class employee:
    @staticmethod
    def display():
        print('HI I AM ROSHAN')
    def show1(self):
        self.name="Roshan"
        self.loc="Hyd"
        self.street="uppal"
    def display1(self):
        print("Name:",self.name)
        print("Location:",self.loc)
        print("Street:",self.street)

e=employee()
e.display()
e.show1()
e.display1()
