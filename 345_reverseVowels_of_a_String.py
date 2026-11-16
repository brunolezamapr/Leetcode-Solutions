

class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = 'AaEeIiOoUu'
        while left < right:
            if not s[left] in vowels:
                left += 1
            elif not s[right] in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.reverseVowels("hello") == "holle", "Fallo 'hello'"
    assert sol.reverseVowels("leetcode") == "leotcede", "Fallo 'leetcode'"
    assert sol.reverseVowels("a") == "a", "Fallo 'a'"
    assert sol.reverseVowels("") == "", "Fallo ''"
    assert sol.reverseVowels("xyz") == "xyz", "Fallo 'xyz' (sin vocales)"
    assert sol.reverseVowels("Aa") == "aA", "Fallo 'Aa'"
    assert sol.reverseVowels("abba") == "abba", "Fallo 'abba'"
    assert sol.reverseVowels("AaEeIiOoUu") == "UuOoIiEeAa", "Fallo 'AaEeIiOoUu'"
    assert sol.reverseVowels("aA") == "Aa", "Fallo 'aA'"
    assert sol.reverseVowels("rhythm") == "rhythm", "Fallo 'rhythm' (sin vocales)"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   