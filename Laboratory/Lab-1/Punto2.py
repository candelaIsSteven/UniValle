'''
Programa que pida la temperatura en grados Celsius y la convierta a grados Fahrenheit mostrando en pantalla un mensaje del tipo “xxx.xx grados Celsius son yyy.yy grados Fahrenheit”
'''

def main():
  gradosCelsius = float(input("Digite la temperatura en grado Celsius: "))

  gradosFarenheit = celsiusAFarenheit(gradosCelsius)

  print(f"{gradosCelsius} grados Celsius son {gradosFarenheit} grados Farenheit")

def celsiusAFarenheit(gradosCelsius):

  # Formula de Celsius a Farenheit: (gradosCelsius * 9/5) + 32
  gradosFarenheit = (gradosCelsius * 1.8) + 32

  return gradosFarenheit

main()