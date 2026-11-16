
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4, "Fallo [-1,0,3,5,9,12] t=9"
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1, "Fallo [-1,0,3,5,9,12] t=2"
    assert sol.search([5], 5) == 0, "Fallo [5] t=5"
    assert sol.search([5], 3) == -1, "Fallo [5] t=3"
    assert sol.search([1], 1) == 0, "Fallo [1] t=1"
    assert sol.search([1], 2) == -1, "Fallo [1] t=2"
    assert sol.search([1, 2, 3, 4, 5], 1) == 0, "Fallo [1..5] t=1 (primero)"
    assert sol.search([1, 2, 3, 4, 5], 5) == 4, "Fallo [1..5] t=5 (último)"
    assert sol.search([1, 2, 3, 4, 5], 3) == 2, "Fallo [1..5] t=3 (medio)"
    assert sol.search([1, 2, 3, 4, 5], 0) == -1, "Fallo [1..5] t=0 (menor)"
    assert sol.search([1, 2, 3, 4, 5], 6) == -1, "Fallo [1..5] t=6 (mayor)"
    assert sol.search([-5, -3, -1, 0, 2, 4], -3) == 1, "Fallo negativos t=-3"
    assert sol.search([1, 3], 3) == 1, "Fallo [1,3] t=3"
    assert sol.search([1, 3], 2) == -1, "Fallo [1,3] t=2"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   