from typing import List


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i,v in enumerate(nums):
            complement = target - v

            if complement in seen:
                return [seen[complement],i]
            
            seen[v] = i
        
        return []

#Pruebas

def run_tests():
    sol = Solution()
    
    # Caso 1: Ejemplo estándar de LeetCode
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1], "Fallo en Caso 1"
    
    # Caso 2: Otros números
    assert sol.twoSum([3, 2, 4], 6) == [1, 2], "Fallo en Caso 2"
    
    # Caso 3: Números negativos
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4], "Fallo en Caso 3"
    
    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()