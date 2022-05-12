class Car:
    model = "HatchBack"
    color = "Red"
    price = 100000

    @staticmethod
    def drive(self):
        print("car is running")

    def lock(self):
        print("car is locked")

    def unlock(self):
        print("car is unlocked")

    c1 = Car()
    c2 = Car()

    c1.model
