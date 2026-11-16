
class Solution(object):
    def findDisappearedNumbers(self, nums):
        _set = set(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in _set:
                res.append(i)

        return res

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 5, 1]) == [6], "Fallo [4,3,2,7,8,2,5,1]"
    assert sol.findDisappearedNumbers([1]) == [], "Fallo [1]"
    assert sol.findDisappearedNumbers([2]) == [1], "Fallo [2]"
    assert sol.findDisappearedNumbers([1, 2, 3, 4]) == [], "Fallo [1,2,3,4]"
    assert sol.findDisappearedNumbers([2, 2]) == [1], "Fallo [2,2]"
    assert sol.findDisappearedNumbers([3, 3]) == [1, 2], "Fallo [3,3]"
    assert sol.findDisappearedNumbers([1, 1]) == [2], "Fallo [1,1]"
    assert sol.findDisappearedNumbers([5, 4, 3, 2, 1]) == [], "Fallo [5,4,3,2,1]"
    assert sol.findDisappearedNumbers([1, 1, 1, 1]) == [2, 3, 4], "Fallo [1,1,1,1]"
    assert sol.findDisappearedNumbers([2, 3, 2, 4]) == [1], "Fallo [2,3,2,4]"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   