numCoin = int(input())
cost = list(map(int, input().split()))
cost.sort()
available_cost=list()

for i in range(numCoin-2):
    sum=cost[i]+cost[i+1]
    available_cost.append(sum)


