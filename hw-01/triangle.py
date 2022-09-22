class TypesOfTriangles:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def isosceles(self):
        return (self.a == self.b and not (self.a == self.c)) or (self.b == self.c and not (self.b == self.a)) or (
                    self.a == self.c and not (self.b == self.a))

    def equilateral(self):
        return (self.a == self.b) and (self.b == self.c)

    def scalene(self):
        return not (self.a == self.b) and not (self.b == self.c) and not (self.a == self.c)

    def right(self):
        if self.c > self.a and self.c > self.b:
            return round((self.a ** 2) + (self.b ** 2)) == round(self.c ** 2)
        elif self.a > self.c and self.a > self.b:
            return round((self.b ** 2) + (self.c ** 2)) == round(self.a ** 2)
        elif self.b > self.a and self.b > self.c:
            return round((self.a ** 2) + (self.c ** 2)) == round(self.b ** 2)

    def classify_triangle(self):
        if self.equilateral():
            if self.right():
                return 'equilateral and right'
            else:
                return 'equilateral'

        elif self.isosceles():
            if self.right():
                return 'isosceles and right'
            else:
                return 'isosceles'

        elif self.scalene():
            if self.right():
                return 'scalene and right'
            else:
                return 'scalene'
