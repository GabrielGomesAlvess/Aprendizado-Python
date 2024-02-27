"""
Faça um programa que fará a leitura de indeterminados números e esses devem ser armazenados em um vetor.
No final devem ser apresentados a soma, a média e o número de elementos desse vetor.
A condição de saída é o usuário digitando o número 0 (zero).
"""

vetor = []
soma = 0
media = 0

while True:
    num = int(input("\nDigite um numero: "))
    opcao = input('Deseja continuar (Digite "0" para parar e "S" para continuar)? \n')
    vetor.append(num)
    if opcao == '0':
       break
quant_num = len(vetor)
soma = sum(vetor)
media = sum(vetor)/len(vetor)

print(f"Numero de elementos: {quant_num}")
print(f"Soma dos elementos: {soma}")
print(f"Media dos elementos: {media:.2f}")
    