class interest_calculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_simple_interest(self):
        return (self.principal * self.rate * self.time) / 100

    def calculate_compound_interest(self):
        return self.principal * ((1 + self.rate / 100) ** self.time - 1)

# Example usage:
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = float(input("Enter the time period (in years): "))

calculator = interest_calculator(principal, rate, time)
simple_interest = calculator.calculate_simple_interest()
compound_interest = calculator.calculate_compound_interest()

print(f"Simple Interest: {simple_interest:.2f}")
print(f"Compound Interest: {compound_interest:.2f}")
print("Thank you for using the interest calculator!")
