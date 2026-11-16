
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1

        while left < len(nums) and right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            right += 1

        return left + 1

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    # [1,1,2] → len=2, nums[:2] == [1,2]
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2], f"Fallo [1,1,2]: k={k}, nums[:k]={nums[:k]}"

    # [0,0,1,1,1,2,2,3,3,4] → len=5, nums[:5] == [0,1,2,3,4]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4], f"Fallo [0,0,1,1,1,2,2,3,3,4]: k={k}, nums[:k]={nums[:k]}"

    # [1] → len=1
    nums = [1]
    k = sol.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [1], f"Fallo [1]: k={k}"

    # [1,1] → len=1
    nums = [1, 1]
    k = sol.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [1], f"Fallo [1,1]: k={k}"

    # [1,2,3] sin duplicados → len=3
    nums = [1, 2, 3]
    k = sol.removeDuplicates(nums)
    assert k == 3 and nums[:k] == [1, 2, 3], f"Fallo [1,2,3]: k={k}"

    # [] → len=0
    nums = []
    k = sol.removeDuplicates(nums)
    assert k == 0, f"Fallo []: k={k}"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   