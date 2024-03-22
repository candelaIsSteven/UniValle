'''
Implementar en Python la siguiente fórmula para calcular el seno de un ángulo medio
'''
import math

def main():
  
  angulo = float(input("Digite el valor del angulo en grados sexagesimales: "))

  resultado = senoAnguloMedio(angulo)

  print(f"El seno del angulo medio de {angulo} es {resultado}")

def senoAnguloMedio(angulo):

  # Convertimos los angulos de grados sexagesimales a radianes
  anguloRadianes = math.radians(angulo)

  # Formula angulo medio = √((1 - cosθ) / 2)
  resSenoAnguloMedio = math.sqrt((1 - math.cos(anguloRadianes)) / 2)

  return resSenoAnguloMedio

main()