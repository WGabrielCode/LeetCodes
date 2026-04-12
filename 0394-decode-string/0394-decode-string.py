class Solution:
    def decodeString(self, s: str) -> str:
        def rec():

            nonlocal i

            if i >= len(s):
                return ""

            chars = ""
            while i < len(s) and 'a' <= s[i] <= 'z':
                chars += s[i]
                i += 1
            if chars:
                return chars

            num = ""
            while i < len(s):
                a = s[i]
                if s[i] == '[':
                    i += 1
                    new_response = ""
                    while i < len(s) and s[i] != ']':
                        new_response += rec()
                    num = int(num)
                    chars += num * new_response
                    num = ""
                    if i >= len(s) or s[i] == ']':
                        i += 1
                        return chars
                num += s[i]
                i += 1
                
        i = 0
        result = []
        while i < len(s):
            result.append(rec())
        return "".join(result)