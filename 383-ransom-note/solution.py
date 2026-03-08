# Ransom Note
# Difficulty: Easy
# Runtime: 27 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/ransom-note/

        for letter in magazine:
            if letter in ransomletters:
                ransomletters[letter] -= 1

                ransomletters[letter] = 1
            else:
                ransomletters[letter] += 1
            if letter in ransomletters:
        for letter in ransomNote:
        ransomletters = {}

        for count in ransomletters.values():
