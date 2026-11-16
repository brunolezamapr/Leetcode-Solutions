
class Solution(object):
    def firstUniqChar(self, s):
        char = {}

        for i in s:
            if i in char:
                char[i] += 1
            else:
                char[i] = 1

        for i, v in enumerate(s):
            if char[v] == 1:
                return i
        return -1

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.firstUniqChar("leetcode") == 0, "Fallo 'leetcode'"
    assert sol.firstUniqChar("loveleetcode") == 2, "Fallo 'loveleetcode'"
    assert sol.firstUniqChar("aabb") == -1, "Fallo 'aabb'"
    assert sol.firstUniqChar("") == -1, "Fallo ''"
    assert sol.firstUniqChar("a") == 0, "Fallo 'a'"
    assert sol.firstUniqChar("aa") == -1, "Fallo 'aa'"
    assert sol.firstUniqChar("aabbc") == 4, "Fallo 'aabbc'"
    assert sol.firstUniqChar("z") == 0, "Fallo 'z'"
    assert sol.firstUniqChar("cc") == -1, "Fallo 'cc'"
    assert sol.firstUniqChar("adafd") == 0, "Fallo 'adafd'"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   