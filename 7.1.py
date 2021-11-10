n = int(input("Введите число: "))

for i in range(1, n):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j)
    print(" ")
