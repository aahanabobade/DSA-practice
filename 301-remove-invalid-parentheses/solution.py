# Remove Invalid Parentheses
# Difficulty: Hard
# Runtime: 122 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/remove-invalid-parentheses/

            # Generate next level
            next_level = set()

            for string in current:
                for i in range(len(string)):

                    # Only remove parentheses
                    if string[i] in '()':
                        new_string = string[:i] + string[i + 1:]
                        next_level.add(new_string)

            current = next_level
