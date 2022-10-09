# 거름돈 500, 100, 50, 10원
# 거슬러 줘 할 돈이 N원(N은 항상 10의 배수)
# 거슬러줘야 할 동전의 최소 개수는?

balance = 200
count = 0

# 큰 단위의 화폐부터 차례대로 확인
list = [500, 100, 50, 10]

for coin in list:
    count += balance // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    balance %= coin

print(count)