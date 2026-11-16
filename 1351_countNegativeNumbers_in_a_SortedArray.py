
class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        return count

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.countNegatives([[4,3,2,-1],[3,2,1,-4],[2,1,1,2],[1,1,1,2]]) == 3, "Fallo grid 4x4"
    assert sol.countNegatives([[3,2],[1,0]]) == 0, "Fallo sin negativos"
    assert sol.countNegatives([[1,2,3],[4,5,6]]) == 0, "Fallo todos positivos"
    assert sol.countNegatives([[-1,-2,-3],[-4,-5,-6]]) == 6, "Fallo todos negativos"
    assert sol.countNegatives([[0,0],[0,0]]) == 0, "Fallo todos ceros"
    assert sol.countNegatives([[-1]]) == 1, "Fallo 1x1 negativo"
    assert sol.countNegatives([[1]]) == 0, "Fallo 1x1 positivo"
    assert sol.countNegatives([[-1,0,1],[2,3,4]]) == 1, "Fallo mixto"
    assert sol.countNegatives([[-3,-2,-1],[0,1,2],[3,4,5]]) == 3, "Fallo diagonal"
    assert sol.countNegatives([[-1,-2,-3,-4],[5,6,7,8]]) == 4, "Fallo fila completa"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   

