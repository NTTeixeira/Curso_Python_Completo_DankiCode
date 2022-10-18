lista = ['Carro', 'Barco', 'Avião']
print(lista)

lista.append("Navio")
#lista.append(["Moto", "Bicicleta"])
lista.extend(["Moto", "Bicicleta"])
lista.insert(0, "Carroça")
print(lista)

print("-" * 225)

for i in range(len(lista)):
    print(i, lista[i])

print("-" * 225)

texto = "carro e avião"
texto = texto.split(" e ")
print(texto)

print("-" * 225)



