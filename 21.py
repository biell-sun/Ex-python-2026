import math

a=int(input("Valor de A\n-"))
b=int(input("Valor de B\n-"))
c=int(input("Valor de C\n-"))

if(a != 0):
            delta = (b*b) - 4*a*c
            if(delta > 0):
                x1 =(-b + math.sqrt(delta))/(2*a)
                x2 =(-b + math.sqrt(delta))/(2*a)
                print("delta:",delta,"\n")
                print("x1",x1,"\n")
            if(delta >= -0.000001 and delta <= 0.000001):
                    x1 = -b/(2*a)
                    print("delta:",delta,"\n")
                    print("x1: ",x1)
            else:
                print("Não existe raízes reais")

else:
    print("Num deu aqui não, doido")