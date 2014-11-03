import unittest
from Figuras import Figuras


class TestFiguras(unittest.TestCase):

    #--------Triangulo--------
    def test_triangulo(self):
        fig = Figuras()
        self.assertEqual(10, fig.Triangulo(5, 4))

    def test_triangulo(self):
        fig = Figuras()
        self.assertEqual(56, fig.Triangulo(14, 8))

    def test_triangulo(self):
        fig = Figuras()
        self.assertEqual(138, fig.Triangulo(23, 12))

    #----------Cuadrado-----------
    def test_cuadrado(self):
        fig = Figuras()
        self.assertEquals(64, fig.Cuadrado(8))

    def test_cuadrado(self):
        fig = Figuras()
        self.assertEquals(9, fig.Cuadrado(3))

    def test_cuadrado(self):
        fig = Figuras()
        self.assertEquals(25, fig.Cuadrado(5))

    #---------Rectangulo-----------
    def test_rectangulo(self):
        fig = Figuras()
        self.assertEquals(40, fig.Rectangulo(5, 8))

    def test_rectangulo(self):
        fig = Figuras()
        self.assertEquals(24, fig.Rectangulo(6, 4))

    def test_rectangulo(self):
        fig = Figuras()
        self.assertEquals(60, fig.Rectangulo(12, 5))

    #---------Circulo------------
    def test_circulo(self):
        fig = Figuras()
        self.assertEquals(201.0624, fig.Circulo(8))

    def test_circulo(self):
        fig = Figuras()
        self.assertEquals(28.27, fig.Circulo(3))

    def test_circulo(self):
        fig = Figuras()
        self.assertEquals(153.9384, fig.Circulo(7))

    #---------Poligono-----------
    def test_poligono(self):
        fig = Figuras()
        self.assertEquals(25, fig.Poligono(5, 10))

    def test_poligono(self):
        fig = Figuras()
        self.assertEquals(80.5, fig.Poligono(7, 23))

    def test_poligono(self):
        fig = Figuras()
        self.assertEquals(97, fig.Poligono(13, 15))

if __name__ == "__main__":
    unittest.main()
