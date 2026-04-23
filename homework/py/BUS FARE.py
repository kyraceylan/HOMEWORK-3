class BUSSFARE:
    def __init__(self, distance):
        self.distance = distance

    def calculate_fare(self):
        if self.distance <= 10:
            return 5
        elif self.distance <= 20:
            return 10
        elif self.distance <= 30:
            return 15
        else:
            return 20
# Example usage:
distance = float(input("Enter the distance traveled (in km): "))
bus_fare = BUSSFARE(distance)
fare = bus_fare.calculate_fare()
print(f"The bus fare for {distance} km is: ${fare}")
print("Thank you for using the bus fare calculator!")