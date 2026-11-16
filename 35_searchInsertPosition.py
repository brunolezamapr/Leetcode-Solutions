
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        nums.sort()

        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (j + i) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return i

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.searchInsert([1,3,5,6], 5) == 2, "Fallo [1,3,5,6] t=5"
    assert sol.searchInsert([1,3,5,6], 2) == 1, "Fallo [1,3,5,6] t=2"
    assert sol.searchInsert([1,3,5,6], 7) == 4, "Fallo [1,3,5,6] t=7"
    assert sol.searchInsert([1,3,5,6], 0) == 0, "Fallo [1,3,5,6] t=0"
    assert sol.searchInsert([1], 0) == 0, "Fallo [1] t=0"
    assert sol.searchInsert([1], 1) == 0, "Fallo [1] t=1"
    assert sol.searchInsert([1], 2) == 1, "Fallo [1] t=2"
    assert sol.searchInsert([1,2,3,4,5], 5) == 4, "Fallo [1,2,3,4,5] t=5"
    assert sol.searchInsert([1,2,3,4,5], 6) == 5, "Fallo [1,2,3,4,5] t=6"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   