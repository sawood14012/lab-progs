def knapsack(v, w, limit, n):
   F = [[0]*(limit+1)for x in range(n+1)]
   for i in range(0,n):
       for j in range(limit+1):
            if j >= w[i]:
                F[i][j] = max(F[i-1][j],F[i-1][j-w[i]]+v[i])
            else:
                F[i][j] = F[i-1][j]
   return F


if __name__ == "__main__":
    v = []
    w = []
    n = int(input("enter the number of items"))
    for i in range(n):
        value = int(input("enter the value of "))
        v.append(value)
        weight = int(input("enter the weight of"))
        w.append(weight)
    limit = int(input("enter the limit of the knapsack"))
    f = knapsack(v, w, limit, n)
    print("Max value:", f[n-1][limit])
    y = limit
    for i in range(n-1, -1, -1):
        if f[i][y] > f[i-1][y]:
            print("item:", i, "Value: ", v[i], "weight ", w[i])
            y = y - w[i]

