class Solution:
    def __init__ (self):
        self.cnt = []
    def add(self, k: int) -> None:
        self.cnt.append(k)
    def checker(self, k : int) -> bool:
        ans = sorted(self.cnt)
        l , r = 0 , len(ans) - 1
        while l < r:
            s = ans[l] + ans[r]
            if s == k:
                return True
            elif s > k:
                r -= 1
            else:
                l += 1
        return False
sol = Solution()
sol.add(1)
sol.add(3)
sol.add(4)
sol.add(6)
sol.add(9)

print(sol.checker(9))
print(sol.checker(15))
print(sol.checker(19))



