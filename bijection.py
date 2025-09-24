# Approach (3 sentences):
# Use two hash maps to enforce a bijection: pattern char -> word and word -> pattern char.
# Split the input string by spaces; if lengths differ from pattern, it's immediately false.
# While scanning pairs, any conflict in either map breaks the bijection, so return False; otherwise True at the end.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        p2w, w2p = {}, {}
        for ch, w in zip(pattern, words):
            if ch in p2w and p2w[ch] != w:
                return False
            if w in w2p and w2p[w] != ch:
                return False
            p2w[ch] = w
            w2p[w] = ch
        return True



