class string_revers:
    def __init__(self, string):
        self.string = string

    def revers(self):
        return self.string[::-1]

# Example usage:
string_input = input("Enter a string to reverse: ")
string_reverser = string_revers(string_input)
reversed_string = string_reverser.revers()
print(f"The reversed string is: {reversed_string}")
print("Thank you for using the string reverser!")
