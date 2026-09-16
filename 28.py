nu1=int(input("Diga um numero ai: "))
nu2=int(input("Diga oto numero ai: "))
nu3=int(input("Diga oto numero ai: "))

if(nu1 > nu2 and nu2 > nu3 and nu1 > nu3):
    print("Esse", nu1, "é maio")
if(nu2 > nu1 and nu1 > nu3 and nu2 > nu3):
    print("Esse", nu2, "é maio")
if(nu3 > nu1 and nu2 > nu1 and nu3 > nu2):
    print("Esse", nu3, "é maio")
if(nu2 > nu3 and nu3 > nu1 and nu2 > nu3):
    print("Esse", nu2, "é maio")
if(nu1 > nu2 and nu3 > nu2 and nu1 > nu3):
    print("Esse", nu1, "é maio")
if(nu1 > nu2 and nu3 > nu2 and nu3 > nu1):
    print("Esse", nu3, "é maio")
if(nu1 > nu2 and nu3 > nu2 and nu1 > nu3):
    print("Esse", nu1, "é maio")