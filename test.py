import random

a = [random.randrange(0, 1000) for _ in range(4)]
print(a)
print(*a)