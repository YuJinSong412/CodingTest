class Calculator:
    def __init__(self, nums):
        self.nums = nums

    def sum(self):
        result=0
        for i in self.nums:
            result += i
        return result

    def avg(self):
        result=0
        for i in self.nums:
            result += i
        return result/len(self.nums)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())
