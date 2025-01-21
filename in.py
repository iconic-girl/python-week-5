class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves in a generic way.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} runs and wags its tail.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims gracefully.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies through the air.")

# Example usage
animals = [
    Animal("Generic Animal"),
    Dog("Buddy"),
    Fish("Nemo"),
    Bird("Tweety")
]

for animal in animals:
    animal.move()