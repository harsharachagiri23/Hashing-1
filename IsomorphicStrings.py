# Approach:
# 1. Maintain two hashmaps to track s->t and t->s mappings.
# 2. For each character pair, check if the existing mapping is consistent in both directions.
# 3. If consistent throughout, return True; otherwise return False.
# Tc : O(n), SC: O(1)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t, map_t_s = {}, {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in map_s_t and map_s_t[ch_s] != ch_t:
                return False
            if ch_t in map_t_s and map_t_s[ch_t] != ch_s:
                return False
            
            map_s_t[ch_s] = ch_t
            map_t_s[ch_t] = ch_s

        return True


