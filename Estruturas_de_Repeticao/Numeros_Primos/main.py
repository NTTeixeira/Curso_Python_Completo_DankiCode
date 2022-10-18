n = int(input("Digite um número:"))

if n > 1:
    for x in range(2, n):
        if n % x == 0:
            print("Esse não é um número primo")
            break
    else:
        print("Esse é um número primo")
else:
    print("Valor inválido para essa operação")

