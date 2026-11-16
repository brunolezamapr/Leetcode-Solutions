
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target + 1) - 1

        if lo <= hi:
            return [lo, hi]
        return [-1, -1]

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.searchRange([5,7,7,8,8,10], 8) == [3, 4], "Fallo [5,7,7,8,8,10] t=8"
    assert sol.searchRange([5,7,7,8,8,10], 6) == [-1, -1], "Fallo [5,7,7,8,8,10] t=6"
    assert sol.searchRange([], 0) == [-1, -1], "Fallo [] t=0"
    assert sol.searchRange([1], 1) == [0, 0], "Fallo [1] t=1"
    assert sol.searchRange([1], 2) == [-1, -1], "Fallo [1] t=2"
    assert sol.searchRange([1,1,1,1], 1) == [0, 3], "Fallo [1,1,1,1] t=1"
    assert sol.searchRange([1,2,3,4,5], 5) == [4, 4], "Fallo [1,2,3,4,5] t=5"
    assert sol.searchRange([1,2,3,4,5], 0) == [-1, -1], "Fallo [1,2,3,4,5] t=0"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   

        