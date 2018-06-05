import math
import random
import time

start = time.clock()
n = random.randint(1,10)
print("logn\t\tn\t\tnlogn\t\tn^2\t\tn^3\t\t2^n\t\tn!\n")
for i in range(1,n+1):
    log = math.log(i)
    nlogn = i*log
    nsq = math.pow(i,2)
    ncb = math.pow(i,3)
    tn = math.pow(2,i)
    fact = math.factorial(i)
    print(log,"\t",i,"\t" ,nlogn,"\t" ,nsq,"\t",ncb,"\t",tn,"\t",fact,"\n")

print(start-time.clock())

