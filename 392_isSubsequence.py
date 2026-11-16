
class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.isSubsequence("abc", "ahbgdc") == True, "Fallo 'abc' in 'ahbgdc'"
    assert sol.isSubsequence("axc", "ahbgdc") == False, "Fallo 'axc' in 'ahbgdc'"
    assert sol.isSubsequence("", "t") == True, "Fallo '' in 't'"
    assert sol.isSubsequence("abc", "") == False, "Fallo 'abc' in ''"
    assert sol.isSubsequence("", "") == True, "Fallo '' in ''"
    assert sol.isSubsequence("a", "a") == True, "Fallo 'a' in 'a'"
    assert sol.isSubsequence("a", "b") == False, "Fallo 'a' in 'b'"
    assert sol.isSubsequence("abc", "abc") == True, "Fallo 'abc' in 'abc'"
    assert sol.isSubsequence("abc", "acb") == False, "Fallo 'abc' in 'acb'"
    assert sol.isSubsequence("ace", "abcde") == True, "Fallo 'ace' in 'abcde'"
    assert sol.isSubsequence("aa", "ab") == False, "Fallo 'aa' in 'ab'"
    assert sol.isSubsequence("aa", "aa") == True, "Fallo 'aa' in 'aa'"
    assert sol.isSubsequence("abc", "ababc") == True, "Fallo 'abc' in 'ababc'"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   