n = input()

result =[]
count = 0
for i in range(len(n)):
    if i < len(n)-1:
        if n[i] == n[i+1]:
            count += 1
        else:
            count += 1
            result.append(n[i] + str(count))
            count = 0
    if i == len(n)-1:
        count += 1
        result.append(n[i]+str(count))

print("".join(result))