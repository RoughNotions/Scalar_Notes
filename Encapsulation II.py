class Class:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.__roll_no = roll_no
        self.__age = age

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no

    def get_roll_no(self):
        return self.__roll_no

    def show(self):
        print("Name", self.name, "Roll", self.__roll_no, "Age", self.__age)


c = Class("Aditya", 6, 21)

c.get_roll_no()
c.get_roll_no()
c.show()
