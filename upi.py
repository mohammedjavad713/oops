
class Payment:
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print("Paid Rs.", amount, "using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI")


class Cash(Payment):
    def pay(self, amount):
        print("Paid Rs.", amount, "using Cash")


c = CreditCard()
u = UPI()
ca = Cash()

c.pay(1000)
u.pay(500)
ca.pay(200)
