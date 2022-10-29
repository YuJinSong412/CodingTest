def avg_numbers(*args):
    result=0
    for i in args:
        result += i
    avg = result / len(args)
    print(avg)


avg_numbers(1,2)
avg_numbers(1,2,3,4,5)
