data = input() #입력을 리스트로 받음

num_origin = len(data)
num_half = int(len(data)/2) # 소수점 안생기게 강제 형변환 생활화 하기

sum_left=0
for i in range(num_half):
    sum_left = sum_left+int(data[i])

sum_right=0
for j in range(num_half,num_origin): # (시작,끝)
    sum_right = sum_right+int(data[j])

if sum_left==sum_right:
    print("LUCKY")
else:
    print("READY")