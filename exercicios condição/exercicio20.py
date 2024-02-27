num = 0 
print("Você deve responder esse interrogatorio apenas com S ou N\n")

resp = input("Telefonou para a vítima?")
if resp.lower() == "s":
 num += 1 
 
resp = input("Esteve no local do crime?")
if resp.lower() == "s":
 num += 1
 
resp = input("Mora perto da vítima?")
if resp.lower() == "s":
 num += 1

resp = input("Devia para a vítima?")
if resp.lower() == "s":
 num += 1
 
resp = input("já trabalhou com a vítima?")
if resp.lower() == "s":
 num += 1


if num < 2:
 print("O interrogado é inocente")
elif num == 2:
 print("O interrogado é suspeito.")
elif num < 5:
 print("O interrogado é cumplice!")
else:
 print("O interrogado é o assassino!!!")
 

