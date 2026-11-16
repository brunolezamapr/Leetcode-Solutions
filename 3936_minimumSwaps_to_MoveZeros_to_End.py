
class Solution(object):
    def minimumSwaps(self, nums):
        i = 0
        j = len(nums) - 1
        count = 0

        while i < j:
            if nums[i] != 0:
                i += 1
            elif nums[j] == 0:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
                i += 1
                j -= 1

        return count

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.minimumSwaps([1, 0, 1, 0, 1]) == 1, "Fallo [1,0,1,0,1]"
    assert sol.minimumSwaps([0, 0, 1, 1]) == 2, "Fallo [0,0,1,1]"
    assert sol.minimumSwaps([1, 1, 1, 0, 0]) == 0, "Fallo [1,1,1,0,0] (ya particionado)"
    assert sol.minimumSwaps([0, 0, 0, 1, 1]) == 2, "Fallo [0,0,0,1,1]"
    assert sol.minimumSwaps([1]) == 0, "Fallo [1]"
    assert sol.minimumSwaps([0]) == 0, "Fallo [0]"
    assert sol.minimumSwaps([1, 0]) == 1, "Fallo [1,0]"
    assert sol.minimumSwaps([0, 1]) == 1, "Fallo [0,1]"
    assert sol.minimumSwaps([1, 1, 0, 0]) == 0, "Fallo [1,1,0,0]"
    assert sol.minimumSwaps([0, 0, 1, 1, 0, 0]) == 2, "Fallo [0,0,1,1,0,0]"
    assert sol.minimumSwaps([0, 1, 0, 1, 0]) == 1, "Fallo [0,1,0,1,0]"
    assert sol.minimumSwaps([0, 0, 0, 1, 1, 1]) == 3, "Fallo [0,0,0,1,1,1]"
    assert sol.minimumSwaps([1, 1, 1, 1]) == 0, "Fallo [1,1,1,1]"
    assert sol.minimumSwaps([0, 0, 0, 0]) == 0, "Fallo [0,0,0,0]"
    assert sol.minimumSwaps([0, 1, 1, 0, 1, 0]) == 2, "Fallo [0,1,1,0,1,0]"
    assert sol.minimumSwaps([1, 0, 0, 0, 1, 1, 0]) == 2, "Fallo [1,0,0,0,1,1,0]"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   