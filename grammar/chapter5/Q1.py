class Calculator:
    def __init__(self):
        self.value=0

    def add(self,val):
        self.value += val


class UpgradeCalculator(Calculator):
    def delete(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.delete(7)

print(cal.value)