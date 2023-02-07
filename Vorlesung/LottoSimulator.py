import random

lotteryNumbers = []

for Number in range(1, 50):
   lotteryNumbers.append(Number)

lotteryNumbersWinner = random.sample(lotteryNumbers, 6)
lotteryNumbersWinner.sort()
print(f"The lottery numbers are:\n{lotteryNumbersWinner}")




"""lotteryNumbers = list(range(1, 50))
print(lotteryNumbers)                    -> einfachere Methode, list(range(x,y))"""