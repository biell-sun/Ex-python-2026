nul1=int(input("primeiro numero: "))
nul2=int(input("primeiro numero: "))
nul3=int(input("primeiro numero: "))

if (nul1 > nul2 and nul2 > nul3):
    print("\n-", nul1, "\n-", nul2, "\n-", nul3)

elif (nul1 > nul2 and nul2 > nul3):
    print("\n-", nul1, "\n-", nul3, "\n-", nul2)

elif (nul2 > nul1 and nul1 > nul3):
    print("\n-", nul2, "\n-", nul1, "\n-", nul3)

elif (nul2 > nul3 and nul3 > nul1):
    print("\n-", nul2, "\n-", nul3, "\n-", nul1)

elif (nul3 > nul1 and nul1 > nul2):
    print("\n-", nul3, "\n-", nul1, "\n-", nul2)

else:
    print("\n- ", nul3, "\n- ", nul2, "\n- ", nul1)