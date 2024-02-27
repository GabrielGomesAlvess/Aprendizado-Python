"""
Faça um programa realiza o cadastro de contatos de uma agenda. Cada contato possui os seguintes atributos: nome, telefone e e-mail.
Desenvolva funcionalidades que
Menu:
1 - Cadastra o registro
2 - Listar toda a agenda
9 - Sair
O programa deverá apresentar o menu acima, e a condição de encerramento é o usuário digitar o "9"
"""

matriz = []

while True:
  cadastro = int(input('Digite "1" para fazer o cadastro, "2" para ver a lista e "9" para sair\n'))

  if cadastro == 1:
    nome = str(input("Nome: "))

    telefone = str(input("Telefone: "))

    email = str(input("E-mail: "))

    matriz.append([nome,telefone,email])

  elif cadastro == 2:
    print(matriz)
 
  elif cadastro == 9:
     print("Sair")

     break





      

