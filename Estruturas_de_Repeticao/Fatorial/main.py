n = int(input("Digite um número: "))


for x in range(n,0,-1):
    if x != 1:
        print(x, end=" x ")
    else:
        print(x)