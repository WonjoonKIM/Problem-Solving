import sys
s = sys.stdin.readline().rstrip()

sum=0
sum2=1
for i in range(len(s)):
    if (int(s[i]) == 0 or int(s[i]) == 1):
        sum = sum + int(s[i])
    else:
        sum2 = sum2 * int(s[i])

if sum2==1:
    print(sum)
else:
    print(sum+sum2)

