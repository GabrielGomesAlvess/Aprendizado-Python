soma = 0
quantidade = 0

while True:

    salario = float(input("Informe o salário: "))
    soma = soma + salario
    quantidade = quantidade + 1
    opcao = input("Deseja continuar (s/n)? ").lower()

    if opcao == 'n':
       break

print(f"A soma dos salários é {soma:.2f}")
media = soma / quantidade
print(f"A media dos salários é {media:.2f}")