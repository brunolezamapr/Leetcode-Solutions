
class Solution(object):
    def minimumRecolors(self, blocks, k):
        current_white = blocks[:k].count('W')
        min_white = current_white

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_white -= 1
            if blocks[i] == 'W':
                current_white += 1
            if current_white < min_white:
                min_white = current_white

        return min_white

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.minimumRecolors("WBBWWBBWBW", 7) == 3, "Fallo 'WBBWWBBWBW' k=7"
    assert sol.minimumRecolors("WBWBBBW", 2) == 0, "Fallo 'WBWBBBW' k=2"
    assert sol.minimumRecolors("WWWW", 4) == 4, "Fallo 'WWWW' k=4"
    assert sol.minimumRecolors("BBBB", 4) == 0, "Fallo 'BBBB' k=4"
    assert sol.minimumRecolors("W", 1) == 1, "Fallo 'W' k=1"
    assert sol.minimumRecolors("B", 1) == 0, "Fallo 'B' k=1"
    assert sol.minimumRecolors("WB", 1) == 0, "Fallo 'WB' k=1"
    assert sol.minimumRecolors("WB", 2) == 1, "Fallo 'WB' k=2"
    assert sol.minimumRecolors("WWBB", 2) == 0, "Fallo 'WWBB' k=2"
    assert sol.minimumRecolors("BWWB", 3) == 2, "Fallo 'BWWB' k=3"
    assert sol.minimumRecolors("WBBWBWBB", 4) == 1, "Fallo 'WBBWBWBB' k=4"
    assert sol.minimumRecolors("WWWWWW", 3) == 3, "Fallo 'WWWWWW' k=3"
    assert sol.minimumRecolors("BBBBBB", 3) == 0, "Fallo 'BBBBBB' k=3"
    assert sol.minimumRecolors("WBWBWB", 3) == 2, "Fallo 'WBWBWB' k=3"
    assert sol.minimumRecolors("WBBBBW", 5) == 1, "Fallo 'WBBBBW' k=5"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   