class Vehicle:
    def __init__(self, discount=""):
        self.discount = discount.lower()

    def apply_discount(self, fare):
        if self.discount in ["student", "senior", "pwd"]:
            return fare * 0.8
        return fare

class Motorcycle(Vehicle):
    def __init__(self, discount=""):
        super().__init__(discount)

    def calculate_fare(self, distance):
        base_fare = 50
        extra_fare = 0
        if distance > 2:
            extra_fare = (distance - 2) * 10
        total = base_fare + extra_fare
        return round(self.apply_discount(total))

class Taxicab(Vehicle):
    def __init__(self, discount=""):
        super().__init__(discount)

    def calculate_fare(self, distance):
        base_fare = 50
        extra_fare = 0
        if distance > 2:
            extra_fare = (distance - 2) * 15
        total = base_fare + extra_fare
        return round(self.apply_discount(total))
    
class Suv(Vehicle):
    def __init__(self, discount=""):
        super().__init__(discount)

    def calculate_fare(self, distance):
        base_fare = 50
        extra_fare = 0
        if distance > 2:
            extra_fare = (distance - 2) * 15
        total = base_fare + extra_fare
        return round(self.apply_discount(total))