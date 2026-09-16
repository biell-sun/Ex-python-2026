nu1=int(input("Diga o primero numero - "))
nu2=int(input("Diga o segundo numero - "))
op=input("Qual tu quer? [+] ou [-]\n")

if op == "+":
    print("O resultado é [", nu1 + nu2,"]")
elif op == "-":
    print("O resultado é [", nu1 - nu2,"]")
elif oq == "*":
    print("O resultado é * [", nu1 * nu2,"]")
elif oq == "/":
    print("O resultado é / [", nu1 / nu2,"]")
else:
    print("algo de errado não esta certo!")