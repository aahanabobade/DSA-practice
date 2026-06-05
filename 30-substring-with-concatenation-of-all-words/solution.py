# Substring with Concatenation of All Words
# Difficulty: Hard
# Runtime: 23 ms
# Memory: 13.4 MB
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_length = len(words[0])
        result = []

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        for i in range(word_length):
            left = i
            sub_count = {}
            count = 0

            for j in range(i, len(s) - word_length + 1, word_length):
                sub_word = s[j:j + word_length]

                if sub_word not in word_count:
                    sub_count.clear()
                    count = 0
                    left = j + word_length
                    continue

                sub_count[sub_word] = sub_count.get(sub_word, 0) + 1
                count += 1

                # shrink window if too many of sub_word
                while sub_count[sub_word] > word_count[sub_word]:
                    left_word = s[left:left + word_length]
                    sub_count[left_word] -= 1
                    count -= 1
                    left += word_length

                if count == len(words):
                    result.append(left)

        return result
