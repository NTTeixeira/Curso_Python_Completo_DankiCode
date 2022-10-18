lista = ['Carro', 'Barco', 'avião', 'trem', 'Metro']
print(lista)

print("-" * 225)
# lista.pop() #Remove o último index
# lista.remove("Carro") #Remove o index especificado
# del lista[1] #Remove o index especificado
# lista.clear() #limpa a lista
# lista.sort() #Coloca a lista em ordem(OBS: Ele ordena pelas inicias maiúsculas e minúsculas)
lista.sort(key=str.lower)  # Coloca a lista em ordem(OBS: Ele ordena pelas inicias maiúsculas e minúsculas)

for i in range(len(lista)):
    print(i, lista[i])

print("-" * 225)

lista2 = [2, 3, 5, 1, 4]
# lista2.sort() #Coloca a lista em ordem
# lista2.sort(reverse = True) #Coloca a lista em ordem contrária
lista2.reverse()  # Inverte a sequencia da lista
print(lista2)
