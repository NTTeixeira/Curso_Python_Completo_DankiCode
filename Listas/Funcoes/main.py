lista = ["Chigado", "Queens", "Salvador", "Pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6.3]
print(lista3)

lista4 = [True, False]
print(lista4)

lista5 = [True, "Chicago", "2.5", False, 4]
print(lista5)
print("-" * 225)

lista2 = lista2 + lista3
print(lista2)
print("Tamanho da Lista 2 = ", len(lista2))
print("Soma dos valores da Lista 2 = ", sum(lista2))
print("Maior valor Lista 2 = ", max(lista2))
print("Menor valor Lista 2 = ", min(lista2))
print("-" * 225)

lista6 = list(range(10))
print(lista6)
elemento = 7
if elemento in lista6:
    print("Está dentro da lista")

lista7 = list("Curso de Python")
print(lista7)




