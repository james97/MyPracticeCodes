class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if self.is_palindrome(s) or not s:
            return s

        has_palindrome = False
        for i in xrange(1, len(s)/2):
            if self.is_palindrome(s[:len(s) - i]):
                has_palindrome = True
                break

        if not has_palindrome:
            revseres = "".join(s[:0:-1])
            return revseres+s
        else:
            reverses = ""
            print s[len(s) - i:]
            tmp = s[len(s) - i:]
            reverses = "".join(tmp[::-1])
            return reverses + s


    def is_palindrome(self, s):
        for i in xrange(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print sol.shortestPalindrome("abbacd")