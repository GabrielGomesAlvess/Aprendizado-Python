"""
Uma empresa precisa de um programa que realiza o cadastro de seus produtos, com os seguintes valores: nome, preço, quantidade.
A cada interação deve perguntar se o usuário deseja continuar, a resposta for igual a 'n', o programa encerrará a execução.
No final, deverá ser apresentado o valor total do estoque e a quantidade de produtos cadastrados.
"""


quantidade = 0

while True: 
    nome = str(input("Nome do produto: "))
    preco = eval(input("Preço do produto: "))
    quant = int(input("Quantidade no estoque: "))
    quantidade += 1
    
    soma = quant * preco
    
    print(f"\nNome:{nome}\nValor Total: R${soma:.2f}\nQuantidade:{quant}\n")

    opcao = input("Deseja continuar (s/n)? \n").lower()
    if opcao == 'n':
       break

    

    


