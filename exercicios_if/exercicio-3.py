nota = float(input("digite a nota do aluno:"))

if nota == 8.4:
    print("o aluno tirou uma boa nota!")
elif nota != 0:
    print("o valor e diferente de 7.0")
    if nota >= 8.0:
        print("aluno aprovado!")
    else:
        print("aluno aluno reprovado")