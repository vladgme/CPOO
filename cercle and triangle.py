class Forme:
    def perimeter(self):
        print("")


class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote

    def perimeter(self):
        super().perimeter()
        return self.cote * 4


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimeter(self):
        super().perimeter()
        return (self.longueur + self.largeur) * 2


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def perimeter(self):
        super().perimeter()
        return 2 * 3.14 * self.rayon


class Triangle(Forme):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        super().perimeter()
        return self.a + self.b + self.c


carre = Carre(10)
rectangle = Rectangle(10, 20)
cercle = Cercle(5)
triangle = Triangle(3, 4, 5)

print(carre.perimeter())
print(rectangle.perimeter())
print(cercle.perimeter())
print(triangle.perimeter())
