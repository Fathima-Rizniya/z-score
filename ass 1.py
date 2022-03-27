from statistics import mean,stdev
print("Enter the number of datas = ")
data = []
N = int(input())
for i in range(0,N):
    x = float(input())
    data.append(x)
print("Mean = ",mean(data))
print("Std. Deviation =", stdev(data))

import statistics as s
nd=s.NormalDist(mean(data),stdev(data))
cont=1
while(cont==1):
    print("\n1.Probability lesser than or equal\n2.Probability greater than or equal \n3. Probability between 2 ranges")
    ch=input("Enter(lesser/greater/between) = ")
    if(ch=="lesser"):
        val=float(input("Enter x - "))
        n=nd.cdf(val)
        print("Probability lesser than or equal to",val,"is =",n)
    if(ch=="greater"):
        val=float(input("Enter x - "))
        n=nd.cdf(val)
        print("Probability greater than or equal to",val,"is =",1-n)
    if(ch=="between"):
        val1=float(input("Enter x - "))
        val2=float(input("Enter y - "))
        n=nd.cdf(val2)-nd.cdf(val1)
        print("Probability between",val1,"and ",val2,"is =",n)
        
    cont=int(input("Continue-1 / Stop-0 - "))
    print("NEXT")