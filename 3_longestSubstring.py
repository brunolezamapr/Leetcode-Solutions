from collections import  Counter

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window_counter = Counter()
        longest = 0
        start = 0

        for end in range(len(s)):

            char_end = s[end]
            window_counter[char_end] += 1

            while window_counter[char_end] > 1:
                char_start = s[start]
                window_counter[char_start] -= 1
                start += 1 
            longest = max(end - start + 1,longest)
        
        return longest

#Pruebas
def run_tests():
    sol = Solution()

    assert sol.lengthOfLongestSubstring("abcabcbb") == 3, "Fallo: 'abcabcbb'"
    assert sol.lengthOfLongestSubstring("bbbbb") == 1, "Fallo: 'bbbbb'"
    assert sol.lengthOfLongestSubstring("pwwkew") == 3, "Fallo: 'pwwkew'"
    assert sol.lengthOfLongestSubstring("") == 0, "Fallo: string vacío"
    assert sol.lengthOfLongestSubstring(" ") == 1, "Fallo: un espacio"
    assert sol.lengthOfLongestSubstring("dvdf") == 2, "Fallo: 'dvdf'"
    assert sol.lengthOfLongestSubstring("abcdef") == 6, "Fallo: sin repeticiones"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()

