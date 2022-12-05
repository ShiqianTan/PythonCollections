class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)

        max_substring_length = 0
        idx1 = 0

        for i, char in enumerate(s):
            if i+1 == len(s):
                break
            if s[i+1] not in s[idx1:i+1]:
                max_substring_length = max(max_substring_length, i+2-idx1)
                continue
            else:
                idx1 = idx1 + s[idx1:i+1].index(s[i+1])
                max_substring_length = max(max_substring_length, i+1-idx1)
                idx1 += 1

        return max_substring_length