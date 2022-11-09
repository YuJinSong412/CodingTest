def binary_search(start, end, array, target):

        if start > end:
            return None
        mid = (start + end) // 2

        if array[mid] < target:
            return binary_search(mid+1, end, array, target)
        elif array[mid] > target:
            return binary_search(start, mid-1, array, target)
        elif array[mid] == target:
            return mid




n = int(input())
array = list(map(int,input().split()))
m = int(input())
lists = list(map(int,input().split()))

array.sort()

start = 0
end = n - 1

for i in lists:
    result = binary_search(start, end, array, i)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")

# from bisect import bisect_left
#
# N = int(input())
# produce = list(map(int, input().split()))
# M = int(input())
# consume = list(map(int, input().split()))
#
# produce.sort()
#
# for num in consume:
#     if produce[bisect_left(produce, num)] == num:
#         print("yes", end = ' ')
#     else:
#         print("no", end = ' ')