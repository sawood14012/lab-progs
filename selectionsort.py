import time
import random

n = int(input("enter the no of elements"))

alist = [random.randint(0, 100)for i in range(n)]
print(alist)

start = time.clock()

for i in range(0, n-1):
    least = i
    for j in range(i+1, n):
        if alist[j] < alist[least]:
            least = j
    alist[least], alist[i] = alist[i], alist[least]


print("time taken to sort is %s" % (time.clock()-start))
print(alist)
