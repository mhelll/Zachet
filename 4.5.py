a = range(-3, 3)

print(len([i for i in a if i < 0]))
print(sum([i for i in a if not i % 2 != 0]))
