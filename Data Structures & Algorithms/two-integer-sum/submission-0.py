class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in result_dict:
                return [result_dict[diff], i]
            result_dict[n] = i
        return

        