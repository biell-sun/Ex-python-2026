al=float(input("Quanto tu tem de altura?\n"))
sex=str(input("Qual é o teu sexo?\n [H]Homem [M]Mulher \n_"))

ho = (72.7*al) - 58
mul = (62.1*al) - 44.7

if(sex == "H" or sex == "h"):
    print("Seu peso é esse Caba ", ho)

if(sex == "M" or sex == "m"):
    print("Seu peso é esse muie ", mul)
else:
    print("É o que? ")