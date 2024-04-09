numero1, numero2 = 0, 1

for i in range(50):
    print(numero1)
    numero1, numero2 = numero2, numero1 + numero2
    if i == 50:
        break