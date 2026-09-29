class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        s_list, stack = list(s), []

        if len(s_list)%2 != 0:
            return False

        for i in range(len(s_list)):
            val = s_list[i]
            if val in pairs.keys():
                stack.append(val)
            else:
                if len(stack) == 0:
                    return False
                if val != pairs[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0

