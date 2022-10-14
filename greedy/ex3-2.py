"""
배열의 크기 : N,
숫자가 더해지는 횟수 : M,
숫자를 연속해서 적을 수 있는 횟수 : K

첫째 줄에 N(2<= N <= 1000), M(1<= M <= 10000), K(1<=k<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. (1이상 10000이하의 수로 주어짐)
입력으로 주어지는 K는 항상 M보다 작거나 같다.
"""
import time

N, M, K = map(int,input().split())

data = list(map(int, input().split()))

#start_time = time.time()
data.sort(reverse=True)
#end_time = time.time()

#print("시간측정", end_time - start_time)

result2 = data[0] * K + data[1]

count = M//(K+1)
count2 = M%(K+1)

result = 0
result += result2 * count
result += data[0] * count2

print(result)
