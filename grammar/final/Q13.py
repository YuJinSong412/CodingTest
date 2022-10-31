n = input()

a = list(map(int,n))

result=[]

for i in range(len(a)):
    result.append(str(a[i]))
    if i < len(a)-1:
        if a[i] % 2 ==0 and a[i+1] % 2 == 0:
            result.append("*")
        elif a[i] % 2 != 0 and a[i+1] % 2 != 0:
            result.append(("-"))

print("".join(result))

