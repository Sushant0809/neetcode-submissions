class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        st=[]
        max_area = 0

        for i in range(len(heights)):
            while st and heights[st[-1]]>heights[i]:
                nse = i
                element = st[-1]
                st.pop()
                pse = st[-1] if st else -1

                max_area = max(max_area, heights[element]*(nse-pse-1))
            st.append(i)
        
        while st:
            nse = len(heights)
            element = st[-1]
            st.pop()
            pse = st[-1] if st else -1

            max_area = max(max_area, heights[element]*(nse-pse-1))

        return max_area
            

        