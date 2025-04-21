class Dog:
    def move(self):
        return "Walking"
    
class Bird:
    def move(self):
        return "Flying"
    
class Fish:
    def move(self):
        return "Swimming"
    
class Snake:
    def move(self):
        return "Slithering"
    
class Frog:
    def move(self):
        return "Jumping"
    
dog = Dog()
print(dog.move())  

bird = Bird()
print(bird.move())

fish = Fish()
print(fish.move())

snake = Snake()
print(snake.move())

frog = Frog()
print(frog.move())
        