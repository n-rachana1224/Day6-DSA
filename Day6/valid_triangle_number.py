class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)
        count = 0

        
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:#checking for triangle inequality
                    count += (j - i)   
                    j-=1
                else:
                    i += 1

        return count
num=Solution()
print(num.triangleNumber([2,2,3,4]))