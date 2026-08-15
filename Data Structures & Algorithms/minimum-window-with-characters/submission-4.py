from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        L = R = 0
        t_hashmap = Counter(t)
        s_hashmap = {}
        have=0
        need=len(t_hashmap)

        min_length = len(s) + 1
        sub_string = ""

        while R < len(s):
            char=s[R]
            s_hashmap[char]=s_hashmap.get(char,0)+1

            if char in t_hashmap and s_hashmap[char] == t_hashmap[char]:
                have += 1

            while have == need:

                if R - L + 1 < min_length:
                    min_length = R - L + 1
                    sub_string = s[L:R + 1]

                left_char=s[L]
                s_hashmap[left_char] -= 1

                if left_char in t_hashmap and s_hashmap[left_char] < t_hashmap[left_char]:
                    have -= 1

                if s_hashmap[left_char] == 0:
                    del s_hashmap[left_char]
                    
                L += 1

            R += 1

        return sub_string