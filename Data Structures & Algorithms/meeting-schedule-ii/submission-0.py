"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = []
        end = []


        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        s = 0
        e = 0
        count = 0
        c = 0
        while s<len(start) and e<len(end):

            if start[s]<end[e]:
                c+=1
                s+=1
            else:
                c-=1
                e+=1
            
            count = max(count,c)
        
        return count

        