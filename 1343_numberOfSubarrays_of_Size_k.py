
         
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        current_sum = sum(arr[:k])
        count = 1 if current_sum // k >= threshold else 0

        for i in range(len(arr) - k):
            current_sum -= arr[i]
            current_sum += arr[i + k]

            if current_sum // k >= threshold:
                count += 1

        return count

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.numOfSubarrays([2,2,2,2,5,5,5,8], 2, 4) == 4, "Fallo [2,2,2,2,5,5,5,8] k=2 t=4"
    assert sol.numOfSubarrays([11,13,15,20], 1, 14) == 2, "Fallo [11,13,15,20] k=1 t=14"
    assert sol.numOfSubarrays([11,13,15,20], 1, 100) == 0, "Fallo [11,13,15,20] k=1 t=100"
    assert sol.numOfSubarrays([4,2,1,3,3,1,7,5,2], 7, 3) == 3, "Fallo [4,2,1,3,3,1,7,5,2] k=7 t=3"
    assert sol.numOfSubarrays([1,1,1,1], 2, 1) == 3, "Fallo [1,1,1,1] k=2 t=1"
    assert sol.numOfSubarrays([1,1,1,1], 2, 2) == 0, "Fallo [1,1,1,1] k=2 t=2"
    assert sol.numOfSubarrays([5], 1, 5) == 1, "Fallo [5] k=1 t=5"
    assert sol.numOfSubarrays([5], 1, 6) == 0, "Fallo [5] k=1 t=6"
    assert sol.numOfSubarrays([3,3,3,3,3], 3, 3) == 3, "Fallo [3,3,3,3,3] k=3 t=3"
    assert sol.numOfSubarrays([1,2,3,4,5], 3, 3) == 3, "Fallo [1,2,3,4,5] k=3 t=3"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()  
    