S = input()

count=0
for i in range(len(S)):
    if S[i] == '0':
        count=count+1 #0갯수 파악

if count > (len(S)/2): # 절반 이상이 0이라면
    print("1번")
else:
    print("2번")