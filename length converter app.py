class length_converter:
    def __init__(self, length):
        self.length = length

    def convert_to_miles(self):
        return self.length * 0.621371

    def convert_to_kilometers(self):
        return self.length * 1.60934

    def convert_to_feet(self):
        return self.length * 3280.84

    def convert_to_inches(self):
        return self.length * 39370.1    
# Example usage:
length_input = float(input("Enter a length in meters to convert: "))
converter = length_converter(length_input)
miles = converter.convert_to_miles()
kilometers = converter.convert_to_kilometers()
feet = converter.convert_to_feet()
inches = converter.convert_to_inches()
print(f"{length_input} meters is equal to:")
print(f"{miles:.2f} miles")
print(f"{kilometers:.2f} kilometers")
print(f"{feet:.2f} feet")
print(f"{inches:.2f} inches")
print("Thank you for using the length converter!")
