
def naive_two_sum(nums, target):
    for i in range(len(nums)):
        num = nums[i]
        sub_target = target - num
        for j in range(i +1, len(nums)):
            num_j = nums[j]
            if num_j == sub_target:
                return [i, j]
