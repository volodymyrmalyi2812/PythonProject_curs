class Airplane:
    # Атрибут класа Airplane
    my_count = 0

    # Метод класа Airplane
    def start(self, model, number, color, price):
        self.model = model
        self.color = color
        self.number = number
        self.price = price
        print(f"Hello! I'm a airplane series {self.model}, {self.color}, my tail number is {self.number}, my cost is "
              f"{self.price}$")
        Airplane.my_count += 1


ap1 = Airplane()
ap1.start("Airbus S.A.S", 426, "white", 10000000)
print("Total in aircraft hangar:", ap1.my_count)
print()
ap2 = Airplane()
ap2.start("Boeing", 236, "metallic", 17000000)
print("Total in aircraft hangar:", ap2.my_count)
