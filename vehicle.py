
class Vehicle:
   
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.price)


class Car(Vehicle):
   
    def __init__(self, brand, model, year, price,
                 number_of_doors, fuel_type):
        super().__init__(brand, model, year, price)
        self.number_of_doors = number_of_doors
        self.fuel_type = fuel_type

    def display_info(self):
        print("\n--- Car Details ---")
        super().display_info()
        print("Number of Doors:", self.number_of_doors)
        print("Fuel Type:", self.fuel_type)


class Bike(Vehicle):
  
    def __init__(self, brand, model, year, price,
                 engine_capacity, bike_type):
        super().__init__(brand, model, year, price)
        self.engine_capacity = engine_capacity
        self.bike_type = bike_type

    def display_info(self):
        print("\n--- Bike Details ---")
        super().display_info()
        print("Engine Capacity:", self.engine_capacity, "cc")
        print("Bike Type:", self.bike_type)



car1 = Car("Toyota", "Innova", 2024, 2000000, 4, "Diesel")
bike1 = Bike("Honda", "Shine", 2023, 90000, 125, "Commuter")


car1.display_info()
bike1.display_info()
