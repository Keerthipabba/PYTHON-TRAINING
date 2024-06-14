class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = ""
        for i in range(len(s)):
            b = indices.index(i)
            result += s[b]
        return result
