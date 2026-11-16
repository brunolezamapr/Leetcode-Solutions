
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sorted(sol.intersection([1, 2, 2, 1], [2, 2])) == [2], "Fallo [1,2,2,1] & [2,2]"
    assert sorted(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9], "Fallo [4,9,5] & [9,4,9,8,4]"
    assert sol.intersection([1, 2, 3], [4, 5, 6]) == [], "Fallo sin intersección"
    assert sorted(sol.intersection([1, 1, 1], [1, 1, 1])) == [1], "Fallo [1,1,1] & [1,1,1]"
    assert sol.intersection([], [1, 2, 3]) == [], "Fallo [] & [1,2,3]"
    assert sol.intersection([1, 2, 3], []) == [], "Fallo [1,2,3] & []"
    assert sorted(sol.intersection([1, 2, 2, 3], [2, 2, 4])) == [2], "Fallo [1,2,2,3] & [2,2,4]"
    assert sorted(sol.intersection([-1, 0, 1], [0, 1, 2])) == [0, 1], "Fallo [-1,0,1] & [0,1,2]"
    assert sorted(sol.intersection([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5], "Fallo mismo array"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   