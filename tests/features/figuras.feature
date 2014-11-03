Feature: Obtener el area de figuras geometricas basicas
	Como usuario del sistema 
	Quiero obtener el area de distintas figuras 
	para facilitar algunos calculos


Scenario: "Cuadrado" y el lado el "6" 
	Given: que la figura es un "Cuadrado" y el lado es "6" 
	When: realizo el calculo 
	Then: obtengo el resultado "36"

Scenario: "Cuadrado" y el lado el "8" 
	Given: que la figura es un "Cuadrado" y el lado es "8" 
	When: realizo el calculo 
	Then: obtengo el resultado "64"

Scenario: "Cuadrado" y el lado el "10" 
	Given: que la figura es un "Cuadrado" y el lado es "10" 
	When: realizo el calculo 
	Then: obtengo el resultado "100"

Scenario: "Circulo" y el radio es "3" 
	Given: que la figura es un "Circulo" y el lado es "3" 
	When: realizo el calculo 
	Then: obtengo el resultado con decimales es "28.27"

Scenario: "Circulo" y el radio es "8" 
	Given: que la figura es un "Circulo" y el lado es "8" 
	When: realizo el calculo 
	Then: obtengo el resultado con decimales es "201.06"

Scenario: "Triangulo" su base es "8" y su altura "9" 
	Given: que la figura es un "Triangulo" su base es "8" y su altura "9" 
	When: realizo el calculo 
	Then: obtengo el resultado es "36"