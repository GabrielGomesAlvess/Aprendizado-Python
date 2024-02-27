
lista = [16,-15,14,13,12,-11,10,9,8,7,6,5,-4,3,2,1,0,20,19,18]
for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0
print (lista)