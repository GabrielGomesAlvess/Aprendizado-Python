

 lista = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
for i in range (0,8):
    comeco = lista[i]
    final = lista[15-i]
    lista[i] = final
    lista[15-i] = comeco
print (lista)