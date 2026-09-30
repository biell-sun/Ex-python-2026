num=int(input("diga um numero menor que 1000\n"))

print(f'{int(num/100)} centenas')
print(f'{int((num/10)%10)} dezenas')
print(f'{int((num%100))} unidade')

if num >= 1000:
    print("Para de ser BURRO do caralho!")