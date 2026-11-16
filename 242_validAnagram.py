
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.isAnagram("anagram", "nagaram") == True, "Fallo 'anagram'/'nagaram'"
    assert sol.isAnagram("rat", "car") == False, "Fallo 'rat'/'car'"
    assert sol.isAnagram("a", "ab") == False, "Fallo 'a'/'ab'"
    assert sol.isAnagram("", "") == True, "Fallo ''/''"
    assert sol.isAnagram("a", "a") == True, "Fallo 'a'/'a'"
    assert sol.isAnagram("listen", "silent") == True, "Fallo 'listen'/'silent'"
    assert sol.isAnagram("hello", "olleh") == True, "Fallo 'hello'/'olleh'"
    assert sol.isAnagram("aab", "abb") == False, "Fallo 'aab'/'abb'"
    assert sol.isAnagram("Aa", "aA") == False, "Fallo 'Aa'/'aA' (case-sensitive)"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   