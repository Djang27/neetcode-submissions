class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closedToOpen = {"}" : "{", "]" : "[", ")" : "("}

        for i in s:
            if i not in closedToOpen:
                stack.append(i)
            else:
                if stack and stack[-1] == closedToOpen[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0