from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        n = len(words)

        adj = defaultdict(list)
        ndegree = defaultdict(int)

        unique = 0
        for word in words:
            for ch in word:
                if ch not in ndegree:
                    ndegree[ch] = 0
                    unique+=1

        for i in range(1, n):
            for j in range(min(len(words[i-1]),len(words[i]))):
                if words[i-1][j]!=words[i][j]:
                    adj[words[i-1][j]].append(words[i][j])
                    ndegree[words[i][j]]+=1
                    break
                elif j == min(len(words[i-1]), len(words[i])) - 1:
                    if len(words[i-1]) > len(words[i]):
                        return ""
        
        queue = deque()

        
        for ch in ndegree:
            if ndegree[ch] == 0:
                queue.append(ch)
        
        unique_word = ""

        while queue:
            s = queue.popleft()

            unique_word+=s

            for ele in adj[s]:
                ndegree[ele]-=1
                if ndegree[ele]==0:
                    queue.append(ele)
        
        if len(unique_word)!=unique:
            return ""
        
        return unique_word


        
        