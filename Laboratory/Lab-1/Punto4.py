"""
En matemáticas financieras se tiene la siguiente fórmula para calcular el factor de recuperación de capital, dado un valor presente (p) , una tasa de interés (i), y un número de meses (n).

p = a * (1 + i)^n - 1 / i * (1 + i)^n 

Crear un programa que permita calcular el factor de recuperación de capital para un valor presente, tasa de interés y número de meses dado como entrada por el usuario
"""

def main():
  valorPresente = float(input("Digite el valor presente: "))
  tasaInteres = float(input("Digite la tasa de interes: "))
  meses = int(input("Digite el numero de meses: "))

  resultado = factorRecuperacionCapital(valorPresente, tasaInteres, meses)

  print(f"El factor de recuperación de capital para el valor presente ${valorPresente}, tasa de interés de {tasaInteres}%E.M por {meses} meses es: ${round(resultado,2)}")

def factorRecuperacionCapital(p, i, n):
  a = p / ((1-(1+i/100)**-n)/(i/100) ) # valor presente (p) , tasa de interés (i), y número de meses (n)
  return a

main()