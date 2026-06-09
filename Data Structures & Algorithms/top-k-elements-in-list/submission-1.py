class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hash = {}

        for num in nums:

            if num in hash:
                hash[num]+=1
            
            else:
                hash[num] = 1

        print(hash)
        hash = dict(sorted(hash.items(), key=lambda x:x[1], reverse=True)[:k])

        ans = list(hash.keys())

        print(ans)

        return ans


        