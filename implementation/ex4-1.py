import time

N = int(input())

data = list(input().split())


start = time.time()
x = 1
y = 1

for i in data:
  if(i == "R"):
    if(y + 1 > N):
      y -= 1
    y += 1
  elif(i == "L"):
    if(y - 1 < 1):
      y += 1
    y -= 1
  elif(i == "U"):
    if(x - 1 < 1):
      x += 1
    x -= 1
  elif(i == "D"):
    if(x + 1 > N):
      x -= 1
    x += 1

print(x, y)
print(f"{time.time() - start:.5f} sec")