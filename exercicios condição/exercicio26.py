dia = int(input('Informe  dia que você nasceu: '))
mes = int(input('Informe o mes que você nasceu: '))
ano = eval(input('Informe o ano que você nasceu: '))

if dia <= 31:
    print()
    
if mes <= 12:
    print(dia,'/',mes,'/',ano)
    
    
else:
    print("erro")

