class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        def isPalindrome(s):
            if len(s) <= 2:
                return s[0] == s[-1]
            if s[0] == s[-1]:
                return isPalindrome(s[1:-1])
            else:
                return False

        def odd_Palindrome(s):
            res1 = s[0]
            length = len(s)
            if length % 2 == 1:
                p2 = c2 = length // 2
                while p2 <= length-1:
                    # while p2+1 < length and s[p2+1] == s[p2] :
                    #         p2 += 1
                    if c2-1 >= 0 and p2+1 < length and s[c2-1] == s[p2+1]:
                        c2 -= 1
                        p2 += 1
                        continue
                    if isPalindrome(s[c2:p2+1]):
                        res1 = res1 if len(res1) >= len(s[c2:p2+1]) else s[c2:p2+1]
                        # res1 = res1 if len(res1) >= len(s[c2:p2+1]) else s[c2:p2+1]
                    if p2+1 < length and s[p2+1] == s[p2]:
                        p2 += 1
                    elif c2-1 >= 0 and s[c2-1] == s[c2]:
                        c2 -= 1
                    else:
                        c2 += 1
                        p2 += 1
            return res1
        res1 = s[0]
        length = len(s)
        if length % 2 == 1:
            return odd_Palindrome(s)
        else:
            if len(s) == 2:
                if isPalindrome(s):
                    return s
                else:
                    return s[0]
            c2 = length // 2 - 1
            p2 = c2 + 1
            if s[c2] == s[p2]:
                while p2 <= length-1:
                    # while p2+1 < length and s[p2+1] == s[p2] :
                    #         p2 += 1
                    if c2-1 >= 0 and p2+1 < length and s[c2-1] == s[p2+1]:
                        c2 -= 1
                        p2 += 1
                    if isPalindrome(s[c2:p2+1]):
                        res1 = res1 if len(res1) >= len(s[c2:p2+1]) else s[c2:p2+1]
                        # res1 = res1 if len(res1) >= len(s[c2:p2+1]) else s[c2:p2+1]
                    if p2+1 < length and s[p2+1] == s[p2]:
                        p2 += 1
                    elif c2-1 >= 0 and s[c2-1] == s[c2]:
                        c2 -= 1
                    else:
                        c2 += 1
                        p2 += 1
            else:
                res1 = odd_Palindrome(s[:p2+1])
                res2 = odd_Palindrome(s[c2:])
                res1 = res1 if len(res1) >= len(res2) else res2

        return res1
    

if __name__ == '__main__':
    s = Solution()
    res = s.longestPalindrome('abb')
    assert res == 'bb'
    res = s.longestPalindrome('babad')
    assert res == 'aba'
    res = s.longestPalindrome('aaaa')
    assert res == 'aaaa'
    res = s.longestPalindrome('adam')
    print(res)
    assert res == 'ada'
    res = s.longestPalindrome('abcba')
    print(res)
    assert res == 'abcba'
