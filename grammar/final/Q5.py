def Phvo(num):
    a = 0
    b = 1

    r = 0
    print(a,b, end= " ")
    while r < 13:
        r = a+b
        a = b
        b = r
        print(r, end=" ")

Phvo(13)