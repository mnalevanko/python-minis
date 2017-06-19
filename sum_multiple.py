def sum_multiple(*nums):

    if len(nums) == 0:
        raise AttributeError()

    return sum(nums)

print(sum_multiple())
