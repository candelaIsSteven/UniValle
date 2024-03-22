'''
Una empresa constructora vende terrenos con la forma A de la siguiente figura. Realice un algoritmo e implemente en Python para obtener el área respectiva de un terreno dado las magnitudes A,B y C.
'''

def main():
  a = float(input("Digite el valor del lado a: "))
  b = float(input("Digite el valor del lado b: "))
  c = float(input("Digite el valor del lado c: "))

  resultado = areaTriangulo(a,b,c) + areaRectangulo(b,c)

  print(f"El terreno tiene un area de {resultado} unidades cuadradas")

def areaTriangulo(a, b, c):

  # Quitamos la altura del rectangulo de la figura para obtener solo la altura del triangulo
  altura = a - c

  # Formula para conseguir el area del triangulo: (altura * base) / 2
  resultadoAreaTriangulo = (altura * b) / 2

  return resultadoAreaTriangulo

def areaRectangulo(b,c):

  # Formula para conseguir el area del rectangulo: altura * base
  resultadoAreaRectangulo = b * c

  return resultadoAreaRectangulo

main()