class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_map = {}
        t_to_s_map = {}
        for s_char, t_char in zip(s, t):
            if s_char in s_to_t_map and s_to_t_map[s_char] != t_char:
                return False
            if t_char in t_to_s_map and t_to_s_map[t_char] != s_char:
                return False
            s_to_t_map[s_char] = t_char
            t_to_s_map[t_char] = s_char

        return True
