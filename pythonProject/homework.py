print("\n                                    --- H O M E W O R K ---")
print("\ntask - 1")
class Transport:
    def __init__(self, model, speed, milage):
        self.model = model
        self.speed = speed
        self. milage = milage

car = Transport("Audi", 130, 1230)
print(f"Car model: {car.model}")
print(f"Speed: {car.speed} km/h")
print(f"Milage: {car.milage}")

print("\ntask - 2")
class Reverse:
    def __init__(self, string):
        self.string = string[:: -1]

String = input("Enter a word: ")
Reversed_string = Reverse(String)
print(Reversed_string.string)

print("\ntask - 3")
class Square:
    def __init__(self, side):
        self.side = side

    def calculation(self):
        perimeter = self.side * 4
        area = self.side ** 2
        return (f"Perimeter: {perimeter}"
                f"\nArea: {area}")

Side = int(input("Enter the side of the square: "))
Calculation = Square(Side)
print(Calculation.calculation())