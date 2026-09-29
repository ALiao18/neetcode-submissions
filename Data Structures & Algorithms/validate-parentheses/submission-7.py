class Solution:
    def isValid(self, s: str) -> bool:
        s_list, stack = list(s), []
        pairs = {
            "[": "]", 
            "{": "}", 
            "(": ")"}

        if len(s_list)%2 != 0:
            return False

        for i in range(len(s_list)):
            if s_list[i] in pairs.keys():
                stack.append(s_list[i])
            else:
                if len(stack) > 0:
                    if s_list[i] == pairs[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                        return False
        return len(stack) == 0
            

