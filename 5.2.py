n = 10
y = 10
x = 5
total = 0
while x > 0:
    x = x - 1
    total = total + n
    n = (n * (100 + y)) / 100
print("Дохуя дней ", total)

# Начав тренировки, спортсмен в первый день пробежал n км.
# Каждый день он увеличивал дневную норму на y% нормы предыдущего дня.
# Какой суммарный путь пробежит спортсмен за x дней?