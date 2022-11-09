def binary_search(start, end, array, target):
    if start > end:
        return None
    mid = (start + end) // 2

    sum = 0
    for i in array:
        if i - mid <= 0:
            sum += 0
        else:
            sum += (i-mid)

    if sum > target:
        return binary_search(mid+1, end, array, target)
    elif sum < target:
        return binary_search(start,mid-1,array,target)
    elif sum == target:
        return mid


input_data = list(map(int,input().split()))
n = input_data[0]
target = input_data[1]

array = list(map(int,input().split()))

array.sort(reverse=True)
start = 0
end = array[0]


result = binary_search(start, end, array, target)
print(result)