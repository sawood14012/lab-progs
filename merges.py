import random
import time

count = 0


def merge_list(left_list,right_list):
    global count
    i, j = 0, 0
    result = []
    while i<len(left_list) and j <len(right_list):
        if left_list[i]<=right_list[j]:
            result.append(left_list[i])
            i = i + 1
        else:
            result.append(right_list[j])
            count = count + (len(left_list) - i)
            j =j + 1
    result = result + left_list[i:]
    result = result + right_list[j:]
    return result


def merge_sort(input_list):
    if len(input_list)<=1:
        return input_list
    else:
        mid = int(len(input_list)/2)
        left_list = merge_sort(input_list[:mid])
        right_list = merge_sort(input_list[mid:])
        return merge_list(left_list, right_list)


n = int(input("enter the no of elements"))
number_list = [random.randint(0,100)for i in range(n)]
print(number_list)
start=time.clock()
print(merge_sort(number_list))
print(time.clock()-start)
print("Number of inversions = ", count, "\n")

