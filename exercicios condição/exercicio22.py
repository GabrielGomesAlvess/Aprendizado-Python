num1 = eval(input("Digite o primeiro numero "))
num2 = eval(input("Digite o segundo numero ")) 
num3 = eval(input("Digite o terceiro numero "))
if num1 > num2 and num1 > num3:
 print("O", num1,"é maior que o", num2,"e o", num3)
 
if num2 > num1 and num2 > num3:
 print("O", num2,"é maior que o", num1,"e o", num3)
 
elif num3 > num1 and num3 > num2:
 print("O", num3,"é maio que o",num1,"e o",num3)
 
else:
    print("erro")

 

