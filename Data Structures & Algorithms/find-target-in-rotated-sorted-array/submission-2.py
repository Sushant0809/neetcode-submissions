class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums)-1

        while lo<hi:
            mid = (lo+hi)//2
            if nums[mid]>=nums[hi]:
                lo = mid+1
            else:
                hi = mid
        
        pivot = lo

        lo = 0
        hi = len(nums)-1

        while lo<=hi:
            mid = (lo+hi)//2
            real_mid = (mid+pivot)%len(nums)

            if nums[real_mid]==target:
                return real_mid
            elif nums[real_mid]<target:
                lo=mid+1
            else:
                hi=mid-1
        
        return -1


        