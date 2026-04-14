
def two_sum(nums,target):
    hashmap = {} # stores number -> index
    for i, num in enumerate(nums):
        diff = target - num # number needed

        # check if required number already seen
        if diff in hashmap:
            return [hashmap[diff],i]

        # store current number with index
        hashmap[num] = i


print(two_sum(nums=[3, 2, 4],target=6))