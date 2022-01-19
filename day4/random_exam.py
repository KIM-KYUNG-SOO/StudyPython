# Random 함수
import random #from random import*

# print(random.choice(range(1,7))) # 주사위

# Lottery
numbers = list(range(1,46))
lottery = [] # list

# for i in range(6):
#     lottery.append(random.choice(numbers))

# print(lottery)

lottery.append(random.sample(numbers,6))
lottery.sort()

print(lottery)