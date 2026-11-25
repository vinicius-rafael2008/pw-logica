nota = input("digite seu nome: ")

imc = int(input("peso"))
imc = int(input("altura"))

if imc < 18.5:
    print("abaixo do peso:")

    if imc < 25:
        print("peso normal:")
        
        if imc < 30:
            print("sobrepeso")