class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for x,i in enumerate(nums):
            if (target-i) in d:
                return [d[target-i],x]
            d[i]=x
            
