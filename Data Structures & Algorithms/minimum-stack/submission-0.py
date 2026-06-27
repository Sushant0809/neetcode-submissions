class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append([val,val])
        else:
            mini = min(val, self.st[-1][1])
            self.st.append([val,mini])
        

    def pop(self) -> None:
        if self.st:
            self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]

        
