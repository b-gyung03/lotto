import random

print(random.randint(1, 45))
print(random.choice([10, 20, 30]))
nums = [1, 2, 3, 4, 5]
r = random.shuffle(nums)
print(nums, r)
print(random.sample(range(1, 46), 6))
print(random.sample(range(1, 46), 6))