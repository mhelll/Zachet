a = int(input("Введите число: "))

if a % 2 == 0:
    print("Число кратно 2")
elif str(a)[-1] == str(3):
    print('Число заканчивается на 3')
else:
    print('Числоне кратно 2 и не заканчивается на 3')