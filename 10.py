nu1=int(input("primeiro lado\n-"))
nu2=int(input("segundo lado\n-"))
nu3=int(input("terceiro lado\n-"))

if(nu1+nu2 > nu3 and nu1+nu3 > nu2 and nu2+nu3> nu1):
    if(nu1 != nu2 and nu1 != nu3):
        print("Esse triângulo é escaleno")
    elif(nu1 == nu2 and nu1 == nu3):
        print("Esse triângulo é equilátero")
    else:
        print("Esse triângulo é isósceles")
else:
    print("ISSO NUM É UM TRIÂNGULO, PORRA")
