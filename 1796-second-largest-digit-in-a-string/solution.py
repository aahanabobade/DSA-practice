# Second Largest Digit in a String
# Difficulty: Easy
# Runtime: 7 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/second-largest-digit-in-a-string/

        for ch in s:
            if ch.isdigit():
                num = int(ch)

                if num > largest:
                    second = largest
                    largest = num
                elif largest > num > second:
                    second = num


        second = -1
