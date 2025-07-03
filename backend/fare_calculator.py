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
    
class Jeep(Vehicle):
    def __init__(self):
        super().__init__("Jeep", {"senior_pwd": 0.2, "student": 0.2})

    def calculate_base_fare(self, distance):
        if distance <= 4:
            return 13
        else:
            return 13 + ((distance - 4) * 1.8)


class EJeep(Vehicle):
    def __init__(self):
        super().__init__("EJeep", {"senior_pwd": 0.2, "student": 0.2})

    def calculate_base_fare(self, distance):
        if distance <= 4:
            return 14
        else:
            return 14 + ((distance - 4) * 2.2)


class Bus(Vehicle):
    def __init__(self):
        super().__init__("Bus", {"senior_pwd": 0.2, "student": 0.2})

    def calculate_base_fare(self, distance):
        if distance <= 5:
            return 15
        else:
            return 15 + ((distance - 5) * 2.65)


class LRT:
    stations = [
        "Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go",
        "Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"
    ]

    fare_matrix = [
        [0, 13, 15, 16, 18, 19, 21, 22, 23, 25, 26, 28, 31],
        [13, 0, 13, 15, 17, 18, 19, 21, 22, 24, 25, 27, 29],
        [15, 13, 0, 13, 15, 16, 18, 19, 20, 22, 23, 26, 28],
        [16, 15, 13, 0, 15, 16, 17, 19, 20, 22, 24, 26, 28],
        [18, 17, 15, 15, 0, 14, 16, 17, 18, 20, 21, 24, 26],
        [19, 18, 16, 16, 14, 0, 15, 16, 18, 19, 20, 22, 25],
        [21, 19, 18, 17, 16, 15, 0, 15, 16, 18, 19, 21, 23],
        [22, 21, 19, 19, 17, 16, 15, 0, 15, 16, 17, 19, 21],
        [23, 22, 20, 20, 18, 18, 16, 15, 0, 14, 16, 18, 19],
        [25, 24, 22, 22, 20, 19, 18, 16, 14, 0, 13, 15, 18],
        [26, 25, 23, 24, 21, 20, 19, 17, 16, 13, 0, 15, 16],
        [28, 27, 26, 26, 24, 22, 21, 19, 18, 15, 15, 0, 13],
        [31, 29, 28, 28, 26, 25, 23, 22, 21, 18, 16, 13, 0]
    ]

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def calculate_cost(self):
        if self.start_point not in LRT.stations or self.end_point not in LRT.stations:
            return "Invalid station name"
        i = LRT.stations.index(self.start_point)
        j = LRT.stations.index(self.end_point)
        return LRT.fare_matrix[i][j]

    def calculate_final_cost(self):
        return self.calculate_cost()
