# 재귀함수로 구현
# 입력: 원소의 개수와 찾고자 하는 문자열 입력받기
# 입력: 전체 원소 입력받기
# 출력: 몇 번째 원소인지(없으면 존재하지 않는다는 출력)
# 재귀함수에 넘겨야될 input은? 시작, 끝점, target, array

def binary_search(start, end, target, array):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] > target:
        return binary_search(start, mid -1, target, array)
    elif array[mid] < target:
        return binary_search(mid +1, end, target, array)
    elif array[mid] == target:
        return mid


n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

start = 0
end = n - 1

result = binary_search(start, end, target, array)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
