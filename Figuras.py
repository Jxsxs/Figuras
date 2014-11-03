class Figuras():

    def Triangulo(self, b, h):
        return (b * h) / 2

    def Cuadrado(self, l):
        return l * l

    def Rectangulo(self, b, h):
        return b * h

    def Circulo(self, r):
        return (3.1416 * (r * r))

    def Poligono(self, per, apo):
        return (per * apo) / 2
