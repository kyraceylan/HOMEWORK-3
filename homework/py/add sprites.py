class addsprites:
    def __init__(self, sprite1, sprite2):
        self.sprite1 = sprite1
        self.sprite2 = sprite2

    def add(self):
        return self.sprite1 + self.sprite2
sprite1 = 5
sprite2 = 10
adder = addsprites(sprite1, sprite2)
result = adder.add()
print("The result of adding the sprites is:", result)
