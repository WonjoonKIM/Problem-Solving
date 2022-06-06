food_times = list(map(int, input().split()))
k = int(input())

count=k
while True :
    for i in range(len(food_times)):
        if food_times[i] == 0:
            food_times[i]=food_times[i+1] # 만약 0이면 다음 인덱스 값 가져오기

        food_times[i]=food_times[i]-1
        count-=1 # 1뺏으면 1초 감소
        if count==0: #고장난 시간 동안이 지났으면 break
            break

print( index(food_times[i+1]) ) # 가장 마지막에 연산한 다음 인덱스가 대상 인덱스가 됨


