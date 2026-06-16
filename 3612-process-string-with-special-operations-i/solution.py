# Process String with Special Operations I
# Difficulty: Medium
# Runtime: 55 ms
# Memory: 22.2 MB
# https://leetcode.com/problems/process-string-with-special-operations-i/

            if 'a' <= i <= 'z':
                result.append(i)
            elif i == '*' and result:
                result.pop()
                result.extend(result)
            elif i == '%':
                result.reverse()

        for i in s:

            elif i == '#':
        return "".join(result)
