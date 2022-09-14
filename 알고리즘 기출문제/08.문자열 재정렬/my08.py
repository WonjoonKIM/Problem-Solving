data = input()
data = sorted(data)
'''
리스트.sort()와 sorted(리스트)의 가장 큰 차이는
리스트.sort()는 본체의 리스트를 정렬해서 변환하는 것이고,sorted(리스트)는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것입니다.
]'''
data_list=[]
sum_list=[]

for i in data:
    if i>'9': #str 형태로 비교
        data_list.append(i)
    else:
        sum_list.append(int(i))

data_list.append(sum(sum_list)) #int 형만 sum 가능

result=''
for r in data_list:
    result+=str(r)
print(''.join(result)) #리스트의 데이터를 스트링 형태로 붙임