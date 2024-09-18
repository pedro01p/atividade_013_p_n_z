# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.
val=float(input("informe o numero"))
if val<0:
    print("seu numeo é negativo")
elif val==0:
    print("seu numero é zero")
elif val>0:
    print("seu numero é positivo")