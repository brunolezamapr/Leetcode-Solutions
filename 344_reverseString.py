

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    s = ["h", "e", "l", "l", "o"]
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"], f"Fallo ['h','e','l','l','o']: {s}"

    s = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"], f"Fallo ['H','a','n','n','a','h']: {s}"

    s = ["a"]
    sol.reverseString(s)
    assert s == ["a"], f"Fallo ['a']: {s}"

    s = ["a", "b"]
    sol.reverseString(s)
    assert s == ["b", "a"], f"Fallo ['a','b']: {s}"

    s = ["a", "b", "c"]
    sol.reverseString(s)
    assert s == ["c", "b", "a"], f"Fallo ['a','b','c']: {s}"

    s = ["1", "2", "3", "4", "5", "6"]
    sol.reverseString(s)
    assert s == ["6", "5", "4", "3", "2", "1"], f"Fallo ['1'..'6']: {s}"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   

