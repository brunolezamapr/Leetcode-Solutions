



class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True, "Fallo: 'A man, a plan, a canal: Panama'"
    assert sol.isPalindrome("race a car") == False, "Fallo: 'race a car'"
    assert sol.isPalindrome(" ") == True, "Fallo: ' '"
    assert sol.isPalindrome("") == True, "Fallo: ''"
    assert sol.isPalindrome("a") == True, "Fallo: 'a'"
    assert sol.isPalindrome("ab") == False, "Fallo: 'ab'"
    assert sol.isPalindrome("aA") == True, "Fallo: 'aA'"
    assert sol.isPalindrome("0P") == False, "Fallo: '0P'"
    assert sol.isPalindrome("Was it a car or a cat I saw?") == True, "Fallo: 'Was it a car or a cat I saw?'"
    assert sol.isPalindrome("No 'x' in Nixon") == True, "Fallo: \"No 'x' in Nixon\""

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   