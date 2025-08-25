import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Vous devez spécifier soit le rayon soit le diamètre.")

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area():.2f})"

    # Addition de deux cercles : retourne un nouveau cercle avec rayon = somme des rayons
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    # Comparer quel cercle est plus grand (par rayon)
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    # Comparer quel cercle est plus petit
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    # Vérifier si deux cercles sont égaux (même rayon)
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    # Pour permettre le tri avec sorted()
    def __repr__(self):
        return f"Circle({self.radius})"

c1 = Circle(radius=4)
c2 = Circle(diameter=10)
c3 = Circle(radius=7)

print(c1)  # Circle(radius=4, diameter=8, area=50.27)
print(c2)  # Circle(radius=5, diameter=10, area=78.54)
print(c3)  # Circle(radius=7, diameter=14, area=153.94)

# Addition
c4 = c1 + c2
print(c4)  # Circle(radius=9, diameter=18, area=254.47)

# Comparaisons
print(c1 > c2)  # False
print(c3 == Circle(radius=7))  # True

# Trier les cercles
circles = [c3, c1, c2, c4]
sorted_circles = sorted(circles)
print(sorted_circles)  # [Circle(4), Circle(5), Circle(7), Circle(9)]
