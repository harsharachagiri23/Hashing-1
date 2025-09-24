# Approach:
# 1. Use a hashmap where the key is the sorted version of the word and the value is the list of anagrams.
# 2. For each word, sort its characters, and append the original word into the hashmap at that key.
# 3. Return all the grouped values as the final result.
# TC : O(n * k log k), SC : O(n * k)

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))   
            anagrams[key].append(word)     
        
        return list(anagrams.values())     


