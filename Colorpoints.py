import random
from Point import Point

color = ["red", "blue", "pink", "green", "yellow", "purple", "beige", "bordeaux", "marsala", "peach", "turquoise", "saffron", "magenta"]

class ColoredPoints(Point): # this class inherits from points
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"{self.color}({self.x}, {self.y})"

# lets create a list of 5 random colored points
colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoints(random.randint(-100,100),
                      random.randint(-100,100),
                      random.choice(color)
                      )
    )

print(colored_points)