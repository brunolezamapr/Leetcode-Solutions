

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    # [1,2,3,_,_,_] m=3 + [4,5] n=2 → [1,2,3,4,5]
    nums1 = [1, 2, 3, 0, 0, 0]
    sol.merge(nums1, 3, [4, 5], 2)
    assert nums1 == [1, 2, 3, 4, 5], f"Fallo: {nums1}"

    # [_,_] m=0 + [1,2] n=2 → [1,2]
    nums1 = [0, 0]
    sol.merge(nums1, 0, [1, 2], 2)
    assert nums1 == [1, 2], f"Fallo: {nums1}"

    # [2,_,_] m=1 + [1] n=1 → [1,2]
    nums1 = [2, 0, 0]
    sol.merge(nums1, 1, [1], 2)
    assert nums1[:2] == [1, 2], f"Fallo: {nums1}"

    # [1,_,_] m=1 + [1] n=1 → [1,1]
    nums1 = [1, 0, 0]
    sol.merge(nums1, 1, [1], 1)
    assert nums1[:2] == [1, 1], f"Fallo: {nums1}"

    # [4,5,6,_,_,_] m=3 + [1,2,3] n=3 → [1,2,3,4,5,6]
    nums1 = [4, 5, 6, 0, 0, 0]
    sol.merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6], f"Fallo: {nums1}"

    # [_,_,_] m=0 + [1] n=1 → [1]
    nums1 = [0, 0, 0]
    sol.merge(nums1, 0, [1], 1)
    assert nums1[:1] == [1], f"Fallo: {nums1}"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   