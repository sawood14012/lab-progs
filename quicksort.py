import random
def quicksort(x):
    if len(x)<2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:]if i <= pivot]
        greater = [i for i in x[1:]if i > pivot]
        return quicksort(less)+[pivot]+quicksort(greater)


alist =[random.randint(0,100)for i in range(20)]
print(alist)
print(quicksort(alist))
