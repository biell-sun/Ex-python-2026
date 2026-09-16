mate = (input("Sua materia: "))
u1 = int(input("escreva primeiro numero: "))
u2 = int(input("escreva segundo numero: "))
u3 = int(input("escreva terceiro numero: "))
u4 = int(input("escreva quarto numero: "))

media = (u1 + u2 + u3 + u4) /4

if media >= 7:
    print(f"Sua media é {media} na materia {mate}")
else:
    print(f"Reprovado")