class addmoresprites:
    def __init__(self):
        self.sprites = []

    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    def display_sprites(self):
        for sprite in self.sprites:
            print(sprite)
sprite_manager = addmoresprites()
sprite_manager.add_sprite("alpha")
sprite_manager.add_sprite("beta")
sprite_manager.add_sprite("gamma")
print("The sprites added are:")
sprite_manager.display_sprites()
