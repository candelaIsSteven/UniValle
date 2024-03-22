'''
Crear un programa que calcule la fuerza de atracción gravitacional entre dos masas, M1 y M2 situadas a una distancia R

F =  | (G . m1 . m2) / r² | 

Donde las masas se expresan en kilogramos y la distancia en metros y la constante de gravitación universal vale:

G = 6.672 x 10-11
'''


def main():
  masa1 = float(input("Digite la masa 1 en kilogramos: "))
  masa2 = float(input("Digite la masa 2 en kilogramos: "))
  distancia = float(input("Digita la distacia (en metros) de las dos masas: "))

  fuerza = fuerzaAtraccionGravitacional(masa1, masa2, distancia)

  print(
      f"La fuerza gravitacional entre masa 1 ({masa1} kg) y masa 2 ({masa2} kg) separadas por {distancia} metros, es de {fuerza} Newton"
  )


def fuerzaAtraccionGravitacional(m1, m2, r):
  g = 6.673484 * 10**-11 # Constante de gravitación universal

  # Calculamos la fuerza gravitacional 
  fuerza = abs((g * m1 * m2) / r**2)
  return fuerza


main()
