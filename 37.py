import math

a=int(input("Diga um numero ai pro A-\n"))
b=int(input("Diga um numero ai pro B-\n"))
c=int(input("Diga um numero ai pro C-\n"))

if(a != 0):
    delta = (b*b) - 4*a*c
    print("Delta=", delta,"\n")
    raiz_delta = math.sqrt(delta)
    if(delta == 0):
        x1 = ((-b + raiz_delta)/(2*a))
        print("x1 e x2 é",x1,"\n")
    elif (delta > 0):
        x1 = ((-b + raiz_delta)/(2*a))
        x2 = ((-b - raiz_delta)/(2*a))
        print(f"x1={x1} \nx2= {x2}")
    elif (delta < 0):
        print("Não existe ríz reais!")

else:
    print("Num to entendendo não")