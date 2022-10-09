# 거름돈 500, 100, 50, 10원
# 거슬러 줘 할 돈이 N원(N은 항상 10의 배수)
# 거슬러줘야 할 동전의 최소 개수는?

balance = 1600
count = 0

while balance > 0:
  if balance >= 500:
    count += balance // 500
    balance %= 500
  elif balance >= 100:
    count += balance // 100
    balance %= 100
  elif balance >= 50:
    count += balance // 50
    balance %= 50
  elif balance >= 10:
    count += balance // 10
    balance %= 10

print("count: ", count)
print("balance: ", balance)