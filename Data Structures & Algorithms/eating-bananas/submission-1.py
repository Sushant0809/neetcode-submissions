class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left<right:
            mid = (left+right)//2
            hrs = 0
            for pile in piles:
                if pile%mid==0:
                    hrs+=pile//mid
                else:
                    hrs+=pile//mid+1
            
            if hrs<=h:
                right=mid
            else:
                left = mid+1
        
        return left

        