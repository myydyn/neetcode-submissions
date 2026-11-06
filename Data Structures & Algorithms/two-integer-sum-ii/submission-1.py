class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            while l<=r:
                m = (l+r) // 2
                tmp = target - numbers[i]
                if numbers[m] == tmp:
                    return [i+1, m+1]
                elif numbers[m] < tmp:
                    l = m+1
                else:
                    r = m-1
        return []
