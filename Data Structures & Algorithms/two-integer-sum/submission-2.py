class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, j in enumerate(nums):
            index[j] = i

        values = set(index.keys())
        for i, j in enumerate(nums):
            diff = target - j
            if diff in values and index[diff] != i:
                return [min(index[diff], i), max(index[diff], i)]
