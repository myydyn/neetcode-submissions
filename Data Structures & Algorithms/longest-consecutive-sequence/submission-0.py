class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0,3,2,5,4,6,1,1]
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
    