"""
Para la siguiente figura, se requiere obtener el área de la forma A, Para resolver este problema se puede partir de que está formada por tres figuras: dos triángulos rectángulos, con H como hipotenusa y R como uno de los catetos, que también ese el radio de la otra figura, una semicircunferencia que forma la parte circular (ver forma B). Realice un programa para resolver el problema. Use tres funciones: Una para calcular el área de los dos triángulos, otra para calcular el área de la circunferencia y otra para calcular el área total de la figura. El usuario solo conoce H y R.
"""
import math


def main():

  h = float(input("Digite el valor de H: "))
  r = float(input("Digite el valor de R: "))

  resultado = areaCirculo(r) + areaTriangulo(h, r)

  print(f"El area de la figura es: {round(resultado,2)} unidades cuadradas")


def areaTriangulo(hipotenusa, cateto1):

  cateto2 = math.sqrt(abs(hipotenusa**2 - cateto1**2))

  # Ya que en la figura se muestran dos triangulos con las mismas dimensione y el area
  # del trinagulo es: (cateto1 * cateto2) / 2 -> (cateto1 * cateto2) / 2 * 2 = (cateto1 * cateto2)
  resultadoAreaTriangulo = cateto1 * cateto2

  return resultadoAreaTriangulo


def areaCirculo(radio):

  # Formula area del circulo: πr^2
  # Como es medio circulo -> (πr^2) / 2
  resultadoAreaCirculo = (math.pi * radio**2) / 2

  return resultadoAreaCirculo


main()
