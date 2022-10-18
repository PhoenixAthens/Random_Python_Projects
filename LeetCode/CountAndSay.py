class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.counter(self.countAndSay(n - 1))

    def counter(self, n) -> str:
        arr = []
        counter = 1
        prev = n[0]
        if len(n) == 1:
            arr.append(str(counter))
            arr.append(prev)
        else:
            for i in range(1 , len(n)):
                if n[i] == prev:
                    counter += 1
                else:
                    arr.append(str(counter))
                    arr.append(prev)
                    prev = n[i]
                    counter = 1
                if i==len(n)-1:
                    arr.append(str(counter))
                    arr.append(prev)
        st=""
        for i in arr:
            st += i
        return st


sol = Solution()
print(sol.countAndSay(4))
