
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name)

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.isLongPressedName("alex", "aaleex") == True, "Fallo 'alex'/'aaleex'"
    assert sol.isLongPressedName("saeed", "ssaaedd") == False, "Fallo 'saeed'/'ssaaedd'"
    assert sol.isLongPressedName("leelee", "lleeelee") == True, "Fallo 'leelee'/'lleeelee'"
    assert sol.isLongPressedName("laiden", "laiden") == True, "Fallo 'laiden'/'laiden'"
    assert sol.isLongPressedName("a", "b") == False, "Fallo 'a'/'b'"
    assert sol.isLongPressedName("alex", "aleeexo") == False, "Fallo 'alex'/'aleeexo'"
    assert sol.isLongPressedName("alex", "aalex") == True, "Fallo 'alex'/'aalex'"
    assert sol.isLongPressedName("alex", "alexx") == True, "Fallo 'alex'/'alexx'"
    assert sol.isLongPressedName("alex", "aleex") == True, "Fallo 'alex'/'aleex'"
    assert sol.isLongPressedName("alex", "aleeex") == True, "Fallo 'alex'/'aleeex'"
    assert sol.isLongPressedName("alex", "aleeexx") == True, "Fallo 'alex'/'aleeexx'"
    assert sol.isLongPressedName("alex", "aaleexx") == True, "Fallo 'alex'/'aaleexx'"
    assert sol.isLongPressedName("alex", "aaleeex") == True, "Fallo 'alex'/'aaleeex'"
    assert sol.isLongPressedName("abc", "abbbbc") == True, "Fallo 'abc'/'abbbbc'"
    assert sol.isLongPressedName("abc", "abbbbd") == False, "Fallo 'abc'/'abbbbd'"
    assert sol.isLongPressedName("abc", "abcabc") == False, "Fallo 'abc'/'abcabc'"
    assert sol.isLongPressedName("a", "aa") == True, "Fallo 'a'/'aa'"
    assert sol.isLongPressedName("a", "a") == True, "Fallo 'a'/'a'"
    assert sol.isLongPressedName("ab", "b") == False, "Fallo 'ab'/'b'"
    assert sol.isLongPressedName("ab", "a") == False, "Fallo 'ab'/'a'"
    assert sol.isLongPressedName("abcd", "abccc") == False, "Fallo 'abcd'/'abccc'"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   