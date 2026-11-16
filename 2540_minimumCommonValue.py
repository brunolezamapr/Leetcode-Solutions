
class Solution(object):
    def getCommon(self, nums1, nums2):
        first = 0
        second = 0

        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second]:
                first += 1
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                return nums1[first]

        return -1

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.getCommon([1, 2, 3], [2, 4, 6]) == 2, "Fallo [1,2,3] & [2,4,6]"
    assert sol.getCommon([1, 2, 3], [4, 5, 6]) == -1, "Fallo sin común"
    assert sol.getCommon([1, 1, 2, 7], [3, 4, 7, 8, 9]) == 7, "Fallo [1,1,2,7] & [3,4,7,8,9]"
    assert sol.getCommon([1], [1]) == 1, "Fallo [1] & [1]"
    assert sol.getCommon([1], [2]) == -1, "Fallo [1] & [2]"
    assert sol.getCommon([5, 6, 7], [1, 2, 3]) == -1, "Fallo sin solapamiento"
    assert sol.getCommon([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 1, "Fallo mismo array"
    assert sol.getCommon([2, 4, 6, 8], [1, 3, 5, 7]) == -1, "Fallo par/impar"
    assert sol.getCommon([3, 3, 3], [1, 3, 5]) == 3, "Fallo duplicados"
    assert sol.getCommon([1, 2, 3, 4, 5, 6, 7, 8, 9], [9]) == 9, "Fallo último elemento"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   