# 정렬 라이브러리는 항상 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다.
# 집합 자료형이나 딕셔너리 자료형을 입력받아도 반환되는 결과는 리스트 자료형이다.


#원본을 수정하지않는다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)



#원본을 수정한다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)



# 정렬 라이브러리에서 key를 활용한 코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
# 결과 : [('바나나', 2), ('사과', 5), ('당근', 3)]
