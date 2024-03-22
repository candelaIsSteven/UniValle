'''
Al ingresar a un centro médico se solicitan los siguientes datos para cada paciente: nombre, peso (kg) y altura (mts). Se debe calcular el índice de masa corporal (IMC=peso/altura^2) e identificar la categoría que tiene el paciente según el valor calculado. Hay tres categorías que se pueden identificar según el IMC, éstas son: Infrapeso, Normal y Sobrepeso. Las categorías se calculan utilizando la siguiente tabla:

                        IMC < 18.5         | Infrapeso
                        18.5 <= IMC < 25.0 | Normal
                        IMC >= 25.0        | Sobrepeso

Desarrollar un programa que defina una función donde se calculen los valores de salida para un paciente. Utilizar la función para los tres pacientes que se muestran en la siguiente tabla:

Alex Valencia | 68.3 | 1.72
Maria Caicerdo
'''


def main():

  nombre  = input("Digite el nombre del paciente: ")
  peso  = float(input("Digite el peso del paciente: "))
  altura = float(input("Digite el altura del paciente: "))

  imc_paciente = calcularIMC(peso, altura)
  categoria_paciente = establecerCategoria(imc_paciente)

  print(f"PACIENTE: {nombre}\nIMC: {imc_paciente}\nCategoria: {categoria_paciente}")

def calcularIMC(p, a):
  imc = p / a**2
  return imc

def establecerCategoria(i):
  if i < 18.5:
    categoria = "Infrapeso"
  elif 18.5 <= i < 25:
    categoria = "Normal"
  else:
    categoria = "Sobrepeso"

  return categoria
main()