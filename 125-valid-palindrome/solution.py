# Valid Palindrome
# Difficulty: Easy
# Runtime: 23 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/valid-palindrome/

                ('0'<=s[right] <= '9')
            ):
                right-=1
        
            if s[left].lower() != s[right].lower():
                return False

            left +=1
            right-=1

        return True
            while left<right and not (
                ('a'<=s[right].lower() <= 'z') or

                left+=1
            ):
