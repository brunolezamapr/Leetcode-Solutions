class Solution(object):
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0], "Fallo [0,1,0,3,12]"
    assert sol.moveZeroes([0, 0, 0]) == [0, 0, 0], "Fallo [0,0,0]"
    assert sol.moveZeroes([1, 2, 3]) == [1, 2, 3], "Fallo [1,2,3]"
    assert sol.moveZeroes([0]) == [0], "Fallo [0]"
    assert sol.moveZeroes([1]) == [1], "Fallo [1]"
    assert sol.moveZeroes([0, 1]) == [1, 0], "Fallo [0,1]"
    assert sol.moveZeroes([1, 0]) == [1, 0], "Fallo [1,0]"
    assert sol.moveZeroes([5, 0, 0, 13, 0]) == [5, 13, 0, 0, 0], "Fallo [5,0,0,13,0]"
    assert sol.moveZeroes([-1, 0, 1, 2, 0]) == [-1, 1, 2, 0, 0], "Fallo [-1,0,1,2,0]"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   