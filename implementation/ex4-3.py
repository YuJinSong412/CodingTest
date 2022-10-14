import time
N = input()

start = time.time()

row = int(N[1])  #1
column = N[0]  #a
column_num = ord(column)

steps = [(-2, 1), (-2, -1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

count = 0
for step in steps:
  if row + step[0] >= 1 and row + step[0] <= 8 and column_num + step[1] >= 97 and column_num + step[1] <= 104:
    count += 1

print(count)
print(f"{time.time() - start:.5f} sec")