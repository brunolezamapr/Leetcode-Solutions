
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(i ** 2 for i in nums)

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100], "Fallo [-4,-1,0,3,10]"
    assert sol.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121], "Fallo [-7,-3,2,3,11]"
    assert sol.sortedSquares([0]) == [0], "Fallo [0]"
    assert sol.sortedSquares([1]) == [1], "Fallo [1]"
    assert sol.sortedSquares([-1]) == [1], "Fallo [-1]"
    assert sol.sortedSquares([1, 2, 3]) == [1, 4, 9], "Fallo [1,2,3] (solo positivos)"
    assert sol.sortedSquares([-5, -4, -3]) == [9, 16, 25], "Fallo [-5,-4,-3] (solo negativos)"
    assert sol.sortedSquares([-2, -2]) == [4, 4], "Fallo [-2,-2]"
    assert sol.sortedSquares([2, 2]) == [4, 4], "Fallo [2,2]"
    assert sol.sortedSquares([-100, 100]) == [10000, 10000], "Fallo [-100,100]"
    assert sol.sortedSquares([-1, -1, 1, 1]) == [1, 1, 1, 1], "Fallo [-1,-1,1,1]"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   