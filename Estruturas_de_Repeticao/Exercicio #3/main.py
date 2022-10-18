"""
1-
maior = 0
menor = 0
for i in range(1, 6, 1):
    x = int(input(f"Digite o {i}# valor:"))
    if x > maior:
        maior = x
    if x < menor or menor == 0:
        menor = x
print("Maior = ", maior)
print("Menor = ", menor)
"""
