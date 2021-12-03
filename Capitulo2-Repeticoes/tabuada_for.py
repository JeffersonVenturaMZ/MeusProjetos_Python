tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))

# No range(), definimos que os valores gerados deverão estar entre 1 e 11, com incremento de 1 em 1.
# O “11” foi definido porque ele não se inclui no range, ou seja, quando chegar em 11 ele para, portanto, não executará mais o laço quando atingir este valor.    