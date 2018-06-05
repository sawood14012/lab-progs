import heapq as hq

def dijk(graph,start):
    n = len(graph)
    Q = [[0, start]]
    d = [999 for i in range(n)]
    d[start] = 0
    while Q:
        [length,u]=hq.heappop(Q)
        for v in range(n):
            if d[v] > d[u]+graph[u][v]:
                d[v] = d[u]+graph[u][v]
                hq.heappush(Q,[d[v],u])

    return d



graph = []
#graph = [[0,  5,  10,  999], [5,  0 ,4,  11],[10,  4,  0,  5], [999,  11,  5,0]]

n=int(input("enter the no of nodes"))
print("enter the weights of edges")
for i in range(0,n):
    m=[]
    print("next edge")
    for k in range(0,n):
        print("from",i+1,"to",k+1)
        val = int(input())
        m.append(val)
    graph.append(m)

d=dijk(graph,0)
print(d)


