
class Solution(object):
    def findMaxAverage(self, nums, k):
        avg = sum(nums[:k])
        sum_avg = avg
        for i in range(k, len(nums)):
            avg = avg + nums[i] - nums[i - k]
            if avg > sum_avg:
                sum_avg = avg
        return float(sum_avg) / k

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert abs(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-9, "Fallo [1,12,-5,-6,50,3] k=4"
    assert abs(sol.findMaxAverage([5], 1) - 5.0) < 1e-9, "Fallo [5] k=1"
    assert abs(sol.findMaxAverage([1, 1, 1, 1, 1], 1) - 1.0) < 1e-9, "Fallo [1,1,1,1,1] k=1"
    assert abs(sol.findMaxAverage([1, 1, 1, 1, 1], 5) - 1.0) < 1e-9, "Fallo [1,1,1,1,1] k=5"
    assert abs(sol.findMaxAverage([-1, -2, -3, -4, -5], 2) - -1.5) < 1e-9, "Fallo [-1..-5] k=2"
    assert abs(sol.findMaxAverage([0, 0, 0, 0], 2) - 0.0) < 1e-9, "Fallo [0,0,0,0] k=2"
    assert abs(sol.findMaxAverage([1, 2, 3, 4, 5, 6, 7], 3) - 6.0) < 1e-9, "Fallo [1..7] k=3"
    assert abs(sol.findMaxAverage([100, -100, 100, -100, 100], 3) - 0.0) < 1e-9, "Fallo [100,-100,100,-100,100] k=3"
    assert abs(sol.findMaxAverage([1, 2, 3], 3) - 2.0) < 1e-9, "Fallo [1,2,3] k=3"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   