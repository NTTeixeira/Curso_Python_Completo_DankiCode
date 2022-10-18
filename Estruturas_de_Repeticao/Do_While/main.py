palpite = 0

numero = 9

resp = bool(False)

while not resp:
    palpite = int(input("Qual o número correto? "))
    if palpite == numero:
        print("Certo")
        resp = True
    else:
        print("Errado")
