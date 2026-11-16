
class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0

        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i] != s[i + 2]:
                count += 1
        return count

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.countGoodSubstrings("xyzzaz") == 1, "Fallo 'xyzzaz'"
    assert sol.countGoodSubstrings("abcabc"
) == 4, "Fallo 'abcabc'"
    assert sol.countGoodSubstrings("aabaa") == 0, "Fallo 'aabaa'"
    assert sol.countGoodSubstrings("") == 0, "Fallo ''"
    assert sol.countGoodSubstrings("a") == 0, "Fallo 'a'"
    assert sol.countGoodSubstrings("ab") == 0, "Fallo 'ab'"
    assert sol.countGoodSubstrings("abc") == 1, "Fallo 'abc'"
    assert sol.countGoodSubstrings("aaa") == 0, "Fallo 'aaa'"
    assert sol.countGoodSubstrings("abca") == 2, "Fallo 'abca'"
    assert sol.countGoodSubstrings("xyz") == 1, "Fallo 'xyz'"
    assert sol.countGoodSubstrings("aab") == 0, "Fallo 'aab'"
    assert sol.countGoodSubstrings("aba") == 0, "Fallo 'aba'"
    assert sol.countGoodSubstrings("abcd") == 2, "Fallo 'abcd'"
    assert sol.countGoodSubstrings("aabb") == 0, "Fallo 'aabb'"
    assert sol.countGoodSubstrings("abcdef") == 4, "Fallo 'abcdef'"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   