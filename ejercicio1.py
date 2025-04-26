
(input("ingrese 3 numeros"))
a = 10  # se buscaron 3 numeros y se crearon las variables, luego usando condicionales se busca el numero menor
b = 15
c = 20 

if a < b and a < c: #si
    menor = a
elif b < a and b < c: #combinacion de elseif
    menor = b
else:                   #sino
    menor = c 

print("El numero menor es", menor)