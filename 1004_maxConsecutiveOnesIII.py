
class Solution(object):
    def longestOnes(self, nums, k):
        start = 0
        count_zeros = 0
        longest = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                count_zeros += 1

            while count_zeros > k:
                if nums[start] == 0:
                    count_zeros -= 1
                start += 1

            longest = max(longest, end - start + 1)

        return longest

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6, "Fallo [1,1,1,0,0,0,1,1,1,1,0] k=2"
    assert sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10, "Fallo [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] k=3"
    assert sol.longestOnes([0], 0) == 0, "Fallo [0] k=0"
    assert sol.longestOnes([1], 0) == 1, "Fallo [1] k=0"
    assert sol.longestOnes([0,0,0], 0) == 0, "Fallo [0,0,0] k=0"
    assert sol.longestOnes([0,0,0], 3) == 3, "Fallo [0,0,0] k=3"
    assert sol.longestOnes([1,1,1,1], 0) == 4, "Fallo [1,1,1,1] k=0"
    assert sol.longestOnes([1,0,1,0,1], 1) == 3, "Fallo [1,0,1,0,1] k=1"
    assert sol.longestOnes([1,0,1,0,1], 2) == 5, "Fallo [1,0,1,0,1] k=2"
    assert sol.longestOnes([1,1,0,0,1,1,0,0,1], 2) == 6, "Fallo [1,1,0,0,1,1,0,0,1] k=2"
    assert sol.longestOnes([1,1,1,1,1], 0) == 5, "Fallo [1,1,1,1,1] k=0"
    assert sol.longestOnes([0,0,0,0,0], 0) == 0, "Fallo [0,0,0,0,0] k=0"
    assert sol.longestOnes([0,1,1,0,1,1,1,0,1], 1) == 5, "Fallo [0,1,1,0,1,1,1,0,1] k=1"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()    