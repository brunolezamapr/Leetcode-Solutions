
class Solution(object):
    def missingNumber(self, nums):
       
       nums.sort()

       for i,v in enumerate(nums):

        if i != v:
            return v - 1
        
        if v == len(nums) - 1:
            return v + 1
        

def run_tests():
    sol = Solution()

    assert sol.missingNumber([3, 0, 1]) == 2, "Fallo [3,0,1]"
    assert sol.missingNumber([0, 1]) == 2, "Fallo [0,1]"
    assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8, "Fallo [9,6,4,2,3,5,7,0,1]"
    assert sol.missingNumber([0]) == 1, "Fallo [0]"
    assert sol.missingNumber([1]) == 0, "Fallo [1]"
    assert sol.missingNumber([0, 1, 2, 3, 4]) == 5, "Fallo [0,1,2,3,4]"
    assert sol.missingNumber([1, 2, 3, 4, 5]) == 0, "Fallo [1,2,3,4,5]"
    assert sol.missingNumber([0, 1, 2, 4, 5]) == 3, "Fallo [0,1,2,4,5]"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()