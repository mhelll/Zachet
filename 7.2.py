paws = 64
goose = 2
rabbit = 4

for p in range(1, paws):
    for q in range(1, paws):
        if p * goose + q * rabbit == paws:
            print(f'Гуси: {p:2}         Кролики: {q:2}')





# У гусей и кроликов вместе 64 лапы.
# Сколько могло быть кроликов и гусей (указать все сочетания, которые возможны)?
