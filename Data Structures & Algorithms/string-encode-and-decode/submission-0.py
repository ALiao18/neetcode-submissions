class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += f"{len(s)}_{s}"
        #print(output)
        return output

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '_':
                j += 1
            
            num = int(s[i:j])

            start_str = j+1
            end_str   = start_str + num
            res.append(s[start_str:end_str])

            i = end_str
        
        return res
        
