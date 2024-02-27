#Faça que fará o cálculo do valor de uma prestação em atraso, utilizando a fórmula abaixo
#PRESTAÇÃO = Valor + (Valor * (Taxa / 100) * Tempo)

valor = float(input("Informe o valor: "))
taxa = float(input("Informe o valor da taxa: "))
tempo = float(input("Informe os dias de atraso")) 

valor_total = valor + (valor * (taxa / 100) * tempo)

print (f"O valor da prestação em atraso é de: {valor_total:.2f}")
