from collections.abc import Iterable
#También funciona sin abc

for _ in [list(), range(100), dict(), 5, .5, "ficheros"]:
    if(isinstance(_, Iterable)):
        print(type(_).__name__,"es iterable")
    else:
        print(type(_).__name__,"no es iterable")

lista = list(range(100))

iterador = iter(lista)
nueva_lista = list()

while True:
    try:
        elemento = next(iterador)
        #Operaciones con el elemento
        elemento+=1
        nueva_lista.append(elemento)
    except StopIteration:
        print(nueva_lista)
        break

#Generadores
#Ejemplo: números pares
print(range(0,100,2), end="\n\n")
print(list(range(0,100,2)))

#Un generador se crea devolviendo un valor en una función utilizando la palabra clave función hasta el siguiente yield .

def pares(hasta=100):
    i = 0
    while i <= hasta:
        if i % 2 == 0:
            yield i
        i += 1

print(pares())

pares_ = []
for _ in pares(200):
    pares_.append(_)
print(pares_)

#Comprobación que se genera uno a uno
for v in pares(10**1000):
    if v >= 100:
        break
print("Se ha generado de uno en uno")

"""
for v in list(pares(10**1000)): 
    if v >= 100:
        break
"""


