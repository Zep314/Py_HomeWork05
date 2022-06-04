# для мелких тестов, не для сдачи задания

excess_nums = [12, 18, 20, 24, 30, 36, 40, 42, 48]

limit_nums = 50

ret1 = []
for i in range(24,limit_nums):
    for j in range(len(excess_nums)):
        if not ((i - excess_nums[j]) in excess_nums):
            ret1.append(i)
            break
print(len(ret1))
print(ret1)

ret = []

ret = list(filter(lambda x: ,excess_nums))
print(len(ret))
print(ret)
