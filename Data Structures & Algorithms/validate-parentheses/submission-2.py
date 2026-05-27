class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #stack is last in --> first out
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]: #stack exists + last thing put in stack 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False #return once stack is empty
        
            