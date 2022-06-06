n = list(map(int, input().split()))
n=n[1]
m = list(map(int, input().split()))

count=0
for i in range(len(m)):
    j=i+1
    for j in range(len(m)):
        if m[i] != m[j]:
            count+=1
        elif m[i] == m[j]:
            continue

print(int(count/2)) #같은 연산은 두번해서
