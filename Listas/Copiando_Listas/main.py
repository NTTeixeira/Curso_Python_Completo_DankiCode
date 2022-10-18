lista = ["a", "b", "c", "d", "e"]
lista2 = [1, 2, 5, 6, 3, 4]
lista4 = []

# lista3 = lista + lista2
lista.extend(lista2)
lista4 = lista2.copy()
print(lista)
print(lista4)
