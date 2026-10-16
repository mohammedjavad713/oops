class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        total = self.price * self.quantity
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Price:", total)


name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

p = Product(name, price, quantity)
p.display()