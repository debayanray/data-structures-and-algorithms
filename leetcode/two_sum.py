# https://leetcode.com/problems/two-sum/

def get_indices(nums, target):
    lookup_mapping = {}
    for index, val in enumerate(nums):
        if val in lookup_mapping:
            return [lookup_mapping[val], index]

        lookup_mapping[target - val] = index

    return []


print(get_indices([2,7,11,15], 9))
print(get_indices([3,2,4], 6))
print(get_indices([3,3], 6))
print(get_indices([3,-1], 6))
