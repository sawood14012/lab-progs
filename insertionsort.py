import random
import time

n = int(input("enter the number of elements"))

elements = [random.randint(0, 100) for i in range(n)]
print(elements)

start = time.clock()

for i in range(1, n):
    key = elements[i]
    j = i-1
    while j >= 0 and elements[j] > key:
        elements[j + 1] = elements[j]
        j = j - 1
        elements[j + 1] = key
stop = time.clock()
print(elements)
print(stop-start)
