"""
Uma escola necessita de um programa que armazene as informações dos alunos. Cada aluno possui os seguintes atributos: nome, disciplina, nota1, nota2, nota3, nota4
 
Desenvolva funcionalidades que: 
1) Cadastra os registros 
2) Lista as informações, nesse também deve ser informado a média e a situação desse aluno, se a média for maior ou igual a sete, deverá ser apresentar a palavra "Aprovado", 
senão "Reprovado".
3) Pesquisa pelo nome
4) Alteração. O programa solicitará o nome, se encontrar, o programa solicitará as informações (nome, disciplina, nota1, nota2, nota3, nota4)
5) Excluir. O programa também solicitará o nome para a exclusão
 
9) Sair
"""

boletim = []

while True:
   menu = int(input('\nDigite\n1- para fazer o cadastro\n2- para ver a lista\n3- para pesquisar o nome\n4- alterar informação\n5- para excluir\n9- para sair:\n'))
  
   if menu == 1:
     cadastro = {}
     cadastro["nome"] = input("Informe o seu nome: ")
     cadastro["disciplina"] = input("Informe a disciplina: ")
     cadastro["nota1"] = float(input("Informe a nota do 1° bimestre: "))
     cadastro["nota2"] = float(input("Informe a nota do 2° bimestre: "))
     cadastro["nota3"] = float(input("Informe a nota do 3° bimestre: "))
     cadastro["nota4"] = float(input("Informe a nota do 4° bimestre: "))
     boletim.append(cadastro)

     opcao = input('Deseja continuar? ( S / N ) \n')
   if opcao.lower == 'N':
       break
   
   elif menu == 2:
      media = cadastro["nota1"] + cadastro["nota2"] + cadastro["nota3"] + cadastro["nota4"] / 4
      if media >= 7: 
          print("\nAprovado!")
          print(f"A sua nota final é {media:.1f}\n") 
      else:
         print("Reprovado!")
         print(f"A sua nota final é {media:.1f}\n") 

      opcao = input('Deseja continuar? ( S / N ) \n')
   if opcao.lower == 'N':
       break   
   
   elif menu == 3:
      pesquisa = input ("Informe o nome do aluno: ")
      for i in boletim:
        if i ["nome"].lower() == pesquisa.lower():
         print(i)
        else:
           print("Não encontrado")

   elif menu == 4:
      alterar = input ("Informe o nome do aluno para alterar os dados: ")
      for p in boletim:
        if p ["nome"].lower() == alterar.lower():
         p["nome"] = str(input("Informe o seu nome: "))
         p["disciplina"] = str(input("Informe a disciplina: "))
         p["nota1"] = float(input("Informe a nota do 1° bimestre: "))
         p["nota2"] = float(input("Informe a nota do 2° bimestre: "))
         p["nota3"] = float(input("Informe a nota do 3° bimestre: "))
         p["nota4"] = float(input("Informe a nota do 4° bimestre: "))

   elif menu == 5:
      excluir = input("Informe o nome do aluno para excluir os dados: ")   
      for p in boletim:
        if excluir == p["nome"]:
           boletim.remove(p)
           print("Excluido")
           break
            
   elif menu == 9: 
      fechar = input('Deseja fechar o programa? ( S / N ) \n')
      if fechar == 'S' or fechar == "s":
         print("Até logo!")
         break
