nu1=int(input("Seu primeiro número: "))
nu2=int(input("Seu primeiro número: "))
null=input("Sua operação? [+] ou [-] \n")

if null == "+":
    print("Seu resultado é: ", nu1 + nu2)
elif null == "-":
    print("Seu resultado é: ", nu1 - nu2)
else:
    print("Operação invalido!")