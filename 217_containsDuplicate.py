
class Solution(object):
    def containsDuplicate(self, nums):
         
         _set = set()

         for i in nums:
            if i in _set:
                return True
            else:
                _set.add(i)
         return  False 
         
def run_tests():
    sol = Solution()

    assert sol.containsDuplicate([1, 2, 3, 1]) == True, "Fallo [1,2,3,1]"
    assert sol.containsDuplicate([1, 2, 3, 4]) == False, "Fallo [1,2,3,4]"
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True, "Fallo [1,1,1,3,3,4,3,2,4,2]"
    assert sol.containsDuplicate([]) == False, "Fallo []"
    assert sol.containsDuplicate([1]) == False, "Fallo [1]"
    assert sol.containsDuplicate([1, 1]) == True, "Fallo [1,1]"
    assert sol.containsDuplicate([-1, -1]) == True, "Fallo [-1,-1]"
    assert sol.containsDuplicate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False, "Fallo [0..9]"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()