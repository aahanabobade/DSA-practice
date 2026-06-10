# Text Justification
# Difficulty: Hard
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/text-justification/

                    spaces = even_spaces
                    if k - i < extra:
                        spaces += 1

                    line += " " * spaces

                line += words[j - 1]

            res.append(line)
            i = j

        return res
