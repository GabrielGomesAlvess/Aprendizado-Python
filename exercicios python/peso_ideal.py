"""
Tendo como dados de entrada a altura em metros e o sexo de uma pessoa ("M" masculino e "F"
feminino), construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
- para homens: (72.7*h)-58
- para mulheres: (62.1*h)-44.7
"""

h = float(input("Informe a sua altura com ponto ao inves de virgula: "))
sexo = str(input('\nInfome o seu sexo usando o "M" para masculino e "F" para feminino: '))


if sexo == "M" or sexo == "m":
    calculo = (72.7 * h) - 58
    print(f"\nO seu peso ideal é de {calculo:.2f} kg")

elif sexo == "F" or sexo == "f":

    calculo = (62.1 * h) - 44.7
    print(f"\nO seu peso ideal é de {calculo:.2f} kg")

else:
    print("Letra incorreta \n Apenas M ou F")


