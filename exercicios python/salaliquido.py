valor_hora = float(input("Quanto você recebe por hora? \n"))
ativ_extra = float(input("Quanto você recebeu por atividades extras? \n"))
desconto = float(input("Qual é o valor do desconto? \n"))
hora_trab = int(input("Quantas horas você trabalhou este mês? \n"))


valor_total = (valor_hora * hora_trab) + ativ_extra - desconto

print(f"O seu salario liquido é de R${valor_total:.2f}")

