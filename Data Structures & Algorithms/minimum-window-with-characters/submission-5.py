class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_hashmap = Counter(t)
        s_hashmap = {}

        L = 0
        have = 0
        need = len(t_hashmap)

        min_length = float("inf")
        start = 0

        for R in range(len(s)):

            # Expand the window
            char = s[R]
            s_hashmap[char] = s_hashmap.get(char, 0) + 1

            # This character has just satisfied its requirement
            if char in t_hashmap and s_hashmap[char] == t_hashmap[char]:
                have += 1

            # Window is valid
            while have == need:

                # Record the current valid window
                if R - L + 1 < min_length:
                    min_length = R - L + 1
                    start = L

                # Remove left character
                left_char = s[L]
                s_hashmap[left_char] -= 1

                # We just lost a required character
                if left_char in t_hashmap and s_hashmap[left_char] < t_hashmap[left_char]:
                    have -= 1

                # Remove zero-frequency characters
                if s_hashmap[left_char] == 0:
                    del s_hashmap[left_char]

                L += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]