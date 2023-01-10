


class Solution:
    def func(self, nums):
        if len(nums) == 0:
            raise Exception('No subsequences for empty lists.')
        #base case
        if len(nums) == 1:
            return 1

        # if 2 is first<second
        # if 3 if first<second then 1+ LIS[len2]

        LIS = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

# nums = [5,3,6,1,0,5,7]
# nums = [1,2,3,4,2]
nums = [-5,4,2,2,3,4,4,1,5]

sol = Solution()
print(sol.func(nums))









# with sequence retention
class Solution:
    def func(self, nums):
        if len(nums) == 0:
            raise Exception('No subsequences for empty lists.')
        #base case
        if len(nums) == 1:
            lis_nest = nums[0]
            return 1

        # if 2 is first<second

        # if 3 if first<second then 1+ LIS[len2]

        LIS = [1] * len(nums)
        lis_nest = [[]] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            lis_nest[i] = [nums[i]]
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    if (LIS[i] < 1 + LIS[j]):
                        lis_nest[i] = lis_nest[j].copy()
                        lis_nest[i].insert(0, nums[i])
                        LIS[i] = max(LIS[i], 1 + LIS[j])
                        
        res = max(LIS)
        index = LIS.index(res)
        # return res
        return lis_nest[index]

nums = [-5,4,2,2,3,4,4,1,5]

sol = Solution()
print(sol.func(nums))
