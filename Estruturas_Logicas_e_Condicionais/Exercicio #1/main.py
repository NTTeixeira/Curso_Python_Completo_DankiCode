import math
"""
Exercícios - Python 

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

plataformas para treinar sua lógica: site - uri

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa (??) reais qual 
será o valor do mesmo com desconto de (??)%.
04 - área de um círculo - pi = 3,141592
05 - conversão de reais para dolar
06 -  conversão de dolar para reais

Exercício 1

altura = float(input("Qual a altura do retângulo?\n"))
largura = float(input("Qual a largura do retângulo?\n"))

area = altura * largura

print(f"A área do retângulo é igual a {area}")


Exercício 2

lado = float(input("Qual a medida de um dos lados do quadrado?\n"))

area = lado * lado

print(f"A área do quadrado é igual a {area}")


Exercício 3

valorProduto = float(input("Qual o valor do produto?"))
desconto = int(input("Qual o desconto do produto?"))

valorFinal = valorProduto - (valorProduto * (desconto / 100))

print(f"O valor com desconto ficará R${valorFinal}")


Exercício 4

raio = float(input("Qual o raio do círculo?"))

area = math.pi * math.pow(raio, 2)

print(f"A área do círculo é igual a {area: .2f}")


Exercício 5

dolar = 5.10

qtdReal = float(input("Quantos reais deseja converter para dolar?"))

conversao = qtdReal / dolar

print(f"O total de dólares é igual a {conversao: .2f}")



Exercício 6

dolar = 5.10

qtdDolar = float(input("Quantos dolares deseja converter para reais?"))

conversao = qtdDolar * dolar

print(f"O total de reais é igual a {conversao: .2f}")
"""