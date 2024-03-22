'''
Para los siguientes ejercicios debe escribir mínimo dos funciones. La función principal y una función que se use
en ella.

1. Escriba un programa que calcule la longitud y el área total de tres circunferencias sabiendo que la 1ª de
ellas tiene radio R que será introducido por teclado, la 2ª tiene radio 2R y la 3ª tiene radio 3R
'''
import math

def main():
  radio = float(input("Digite el valor del radio del circulo mas pequeño: "))

  # Los que retorna la funcion calculo(radio) se guardara en las variables respectivamente
  # areaCirculos = resultadoArea    ,    longitudCirculos = resultadoLongitud
  areaCirculos, longitudCirculos = calculo(radio)

  print(f"El area total es {areaCirculos} unidades cuadradas")
  print(f"La longitud total es {longitudCirculos} unidades")

def calculo(radio):
  # Calcula el area total de los circulos = (πr^2) + (2πr^2) + (3πr^2)
  # [ Factorizar ] -> πr^2 (1 + 2 + 3) = 6πr^2
  resultadoArea = 6 * math.pi * radio ** 2

  # Calcula la longitud total de los circulos = (2πr) + (4πr) + (6πr)
  # [ Factorizar ] -> πr (2 + 4 + 6) = 12πr
  resultadoLongitud = 12 * math.pi * radio
  return resultadoArea, resultadoLongitud

main()

