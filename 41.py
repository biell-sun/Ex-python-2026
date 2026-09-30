nul1=int(input("Diga um numero:\n"))
nul2=int(input("Diga um numero:\n"))
nul3=int(input("Diga um numero:\n"))
nul4=int(input("Diga um numero:\n"))
nul5=int(input("Diga um numero:\n"))

if (nul1 > nul2 and nul1 > nul3 and nul1 > nul4 and nul1 > nul5):
    print("O número", nul1, "É maior")

elif (nul2 > nul1 and nul2 > nul3 and nul2 > nul4 and nul2 > nul5):
    print("O número", nul2, "É maior")

elif (nul3 > nul1 and nul3 > nul2 and nul3 > nul4 and nul3 > nul5):
    print("O número", nul3, "É maior")

elif (nul4 > nul1 and nul4 > nul2 and nul4 > nul3 and nul4 > nul5):
    print("O número", nul4, "É maior")

elif (nul5 > nul1 and nul5 > nul2 and nul5 > nul3 and nul5 > nul4):
    print("O número", nul5, "É maior")

else:
    print("É tudo igual nesse diacho")
