n, m = list(map(int, input().split()))

result = 0
for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)

# n, m = map(int, input().split())

# arr = [list(map(int, input().split())) for i in range(n)]
# # 2차원 입력 방법 기억해두기.

# mini = 1
# maxi = 1
# # 선언할 때 함수이름으로 변수명 하지 않도록 조심하자.

# for i in range(n):
#     mini = min(arr[i])
#     if maxi < mini:
#         maxi = mini

# print(maxi)