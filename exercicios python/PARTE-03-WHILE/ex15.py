positivos = 0
n = int(input("Número: "))
while n != 0:
    if n > 0:
        positivos += 1
    n = int(input("Número: "))
print(positivos)