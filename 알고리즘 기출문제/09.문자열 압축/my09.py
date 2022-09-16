import numpy as np

s=input()
new_s=[]
size_s = len(s)
division=np.linsapce(2,size_s,1)
division_list=[11]

division_list[1] = size_s # 1개로 분할할 경우 s길이
count=0
same_count=0
i=1 # 반복문을 위한
for d in range(division): #길이만큼 분할 해봄
    for i in range(size_s - d): # 전체 문자열에 대해 일치하는 지 비교
        if s[i] == s[i+d]:
            count+1
            if count == d: # 분할 길이 만큼 맞아야함
                same_count+1
                new_s.append(s[i], s[i + d])

result = s-new_s
result.append(same_count)
result.append()


#모르겠음