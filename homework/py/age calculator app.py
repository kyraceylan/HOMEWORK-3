class agecalculator:
    def __init__(self, current_year):
        self.current_year = current_year

    def calculate_age(self, birth_year):
        age = self.current_year - birth_year
        return age
# Example usage
current_year = 2026
age_calculator = agecalculator(current_year)
birth_year = int(input("Enter your birth year: "))
age = age_calculator.calculate_age(birth_year)
print(f"Your birth year is {age}, so you are {birth_year} years old. ")