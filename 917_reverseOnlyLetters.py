
class Solution(object):
    def reverseOnlyLetters(self, s):
        str_list = list(s)
        left = 0
        right = len(str_list) - 1

        while left < right:
            if not str_list[left].isalpha():
                left += 1
            elif not str_list[right].isalpha():
                right -= 1
            else:
                str_list[left], str_list[right] = str_list[right], str_list[left]
                left += 1
                right -= 1

        return "".join(str_list)

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.reverseOnlyLetters("ab-cd") == "-cdab", "Fallo 'ab-cd'"
    assert sol.reverseOnlyLetters("a-b") == "b-a", "Fallo 'a-b'"
    assert sol.reverseOnlyLetters("abcd") == "dcba", "Fallo 'abcd'"
    assert sol.reverseOnlyLetters("a") == "a", "Fallo 'a'"
    assert sol.reverseOnlyLetters("") == "", "Fallo ''"
    assert sol.reverseOnlyLetters("ab!cd") == "cd!ab", "Fallo 'ab!cd'"
    assert sol.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!", "Fallo 'Test1ng-Leet=code-Q!'"
    assert sol.reverseOnlyLetters("12345") == "12345", "Fallo '12345' (sin letras)"
    assert sol.reverseOnlyLetters("a1b2c") == "c1b2a", "Fallo 'a1b2c'"
    assert sol.reverseOnlyLetters("a-b-c-d-e") == "e-d-c-b-a", "Fallo 'a-b-c-d-e'"
    assert sol.reverseOnlyLetters("...") == "...", "Fallo '...' (solo puntuación)"
    assert sol.reverseOnlyLetters("aA") == "Aa", "Fallo 'aA'"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   
