
class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_length = float('inf')
        start = 0
        current_sum = 0

        for end in range(len(nums)):
            current_sum += nums[end]

            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1

        return min_length if min_length != float('inf') else 0

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.minSubArrayLen(7, [2,3,1,2,4,3]) == 2, "Fallo t=7 [2,3,1,2,4,3]"
    assert sol.minSubArrayLen(4, [1,4,4]) == 1, "Fallo t=4 [1,4,4]"
    assert sol.minSubArrayLen(11, [1,1,1,1,1]) == 0, "Fallo t=11 [1,1,1,1,1]"
    assert sol.minSubArrayLen(1, [1]) == 1, "Fallo t=1 [1]"
    assert sol.minSubArrayLen(2, [1,1]) == 2, "Fallo t=2 [1,1]"
    assert sol.minSubArrayLen(15, [5,1,3,5]) == 0, "Fallo t=15 [5,1,3,5]"
    assert sol.minSubArrayLen(3, [1,2]) == 2, "Fallo t=3 [1,2]"
    assert sol.minSubArrayLen(100, [1,2,3]) == 0, "Fallo t=100 [1,2,3]"
    assert sol.minSubArrayLen(4, [1,1,4]) == 1, "Fallo t=4 [1,1,4]"
    assert sol.minSubArrayLen(6, [1,2,3]) == 2, "Fallo t=6 [1,2,3]"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   