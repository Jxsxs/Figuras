class Figura:
	def __init__(self,args):
		self.figura = args[0]
		self.parametros = args[1:]

	def getArea(self):
		#diccionario
		figuras={"Cuadrado":self.cuadrado(),"Triangulo":self.triangulo(),"Circulo":self.circulo()}
		return figuras[self.figura]

	def cuadrado(self):
		return self.parametros[0]*self.parametros[0]
	def circulo(self):
		return round(3.1416*float(self.parametros[0])**2,2)
	def triangulo(self):
		return (self.parametros[0]*self.parametros[-1])/2
