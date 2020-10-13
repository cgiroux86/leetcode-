class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        res = 0
        for char in S:
            if char == '(':
                stack.append(')')
            else:
                if len(stack) and stack[-1] == ")":
                    stack.pop()
                else:
                    stack.append('(')
        return len(stack)


s = Solution()
print(s.minAddToMakeValid("())"))
print(s.minAddToMakeValid("((("))
print(s.minAddToMakeValid("()))(("))
