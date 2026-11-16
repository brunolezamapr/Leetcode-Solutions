
class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            suma = numbers[left] + numbers[right]

            if suma == target:
                return [left + 1, right + 1]
            elif suma < target:
                left += 1
            else:
                right -= 1

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2], "Fallo [2,7,11,15] t=9"
    assert sol.twoSum([2, 3, 4], 6) == [1, 3], "Fallo [2,3,4] t=6"
    assert sol.twoSum([-1, 0], -1) == [1, 2], "Fallo [-1,0] t=-1"
    assert sol.twoSum([5, 25, 75], 100) == [2, 3], "Fallo [5,25,75] t=100"
    assert sol.twoSum([0, 9, 27, 45, 45, 49], 81) == [1, 6], "Fallo [0,9,27,45,45,49] t=81"
    assert sol.twoSum([1, 2], 3) == [1, 2], "Fallo [1,2] t=3"
    assert sol.twoSum([3, 3], 6) == [1, 2], "Fallo [3,3] t=6"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   