class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        result = ""

        for i in range(len(s)):
            if s[i] == '*':
               stack.pop()
            else:
                stack.append(s[i])    

        return "".join(stack)  