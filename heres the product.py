class heres_the_product:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def product(self):
        return self.a * self.b
num1 = 5
num2 = 10
product_instance = heres_the_product(num1, num2)
result = product_instance.product()
print(f"The product of {num1} times {num2} is: {result}")
