

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    # [3,2,2,3] val=3 → k=2, nums[:2] == [2,2]
    nums = [3, 2, 2, 3]
    k = sol.removeElement(nums, 3)
    assert k == 2 and sorted(nums[:k]) == [2, 2], f"Fallo [3,2,2,3] val=3: k={k}, nums[:k]={nums[:k]}"

    # [0,1,2,2,3,0,4,2] val=2 → k=5, nums[:5] sin 2s
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = sol.removeElement(nums, 2)
    assert k == 5 and 2 not in nums[:k], f"Fallo [0,1,2,2,3,0,4,2] val=2: k={k}, nums[:k]={nums[:k]}"

    # [1,2,3] val=4 → k=3, sin cambios
    nums = [1, 2, 3]
    k = sol.removeElement(nums, 4)
    assert k == 3 and nums[:k] == [1, 2, 3], f"Fallo [1,2,3] val=4: k={k}"

    # [5,5,5] val=5 → k=0
    nums = [5, 5, 5]
    k = sol.removeElement(nums, 5)
    assert k == 0, f"Fallo [5,5,5] val=5: k={k}"

    # [] val=1 → k=0
    nums = []
    k = sol.removeElement(nums, 1)
    assert k == 0, f"Fallo [] val=1: k={k}"

    # [1] val=1 → k=0
    nums = [1]
    k = sol.removeElement(nums, 1)
    assert k == 0, f"Fallo [1] val=1: k={k}"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   