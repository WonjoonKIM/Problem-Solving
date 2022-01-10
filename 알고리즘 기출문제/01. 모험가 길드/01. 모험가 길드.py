N=int(input())

x=list(map(int, input().split()))

x.sort() # 어느 숫자부터 삭제할 지 정하기 위한 정렬

group=0
while(True):
    for i in range(x[-1]-1): # 마지막 한개는 최대 값을 위해 남겨둠
        x.remove(x[i])
    x.pop()
    group=group+1
    if (len(x)==0 or x[-1] > len(x)):
        break

print(group)

