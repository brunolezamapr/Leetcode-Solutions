
class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                opcion_izq = s[left + 1: right + 1]
                opcion_der = s[left: right]
                return opcion_izq == opcion_izq[::-1] or opcion_der == opcion_der[::-1]
            left += 1
            right -= 1

        return True

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.validPalindrome("abcba") == True, "Fallo 'abcba'"
    assert sol.validPalindrome("abca") == True, "Fallo 'abca'"
    assert sol.validPalindrome("deeea") == False, "Fallo 'deeea'"
    assert sol.validPalindrome("abc") == False, "Fallo 'abc'"
    assert sol.validPalindrome("a") == True, "Fallo 'a'"
    assert sol.validPalindrome("") == True, "Fallo ''"
    assert sol.validPalindrome("ab") == True, "Fallo 'ab'"
    assert sol.validPalindrome("aa") == True, "Fallo 'aa'"
    assert sol.validPalindrome("aba") == True, "Fallo 'aba'"
    assert sol.validPalindrome("abbca") == True, "Fallo 'abbca'"
    assert sol.validPalindrome("abcda") == False, "Fallo 'abcda'"
    assert sol.validPalindrome("aguokepatgbnvxdmgngivhdfumhwoaheryujpntlpkrhongkafoamnpbtiaw") == True, "Fallo caso largo"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   