a = int(input("Введите число: "))
even = 0
odd = 0
while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print("Четных: ", even)
print("Нечетных: ", odd)


# Определить, сколько в введенном пользователем числе четных цифр, а сколько нечетных.