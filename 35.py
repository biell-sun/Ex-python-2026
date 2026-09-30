sal=int(input("Quanto tu quer pintar [Em metros quadrados]\n-"))

litros = sal/3
latas = litros/3

if(latas *18 < litros):
    latas = latas + 1

    valor = latas * 80

print(f"De acordo com a esse coiso {sal}")
print(f"Você precisa de {latas} latas pra pintar isso ai")
