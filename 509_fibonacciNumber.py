

class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.fib(0) == 0, "Fallo fib(0)"
    assert sol.fib(1) == 1, "Fallo fib(1)"
    assert sol.fib(2) == 1, "Fallo fib(2)"
    assert sol.fib(3) == 2, "Fallo fib(3)"
    assert sol.fib(4) == 3, "Fallo fib(4)"
    assert sol.fib(5) == 5, "Fallo fib(5)"
    assert sol.fib(6) == 8, "Fallo fib(6)"
    assert sol.fib(7) == 13, "Fallo fib(7)"
    assert sol.fib(10) == 55, "Fallo fib(10)"
    assert sol.fib(15) == 610, "Fallo fib(15)"
    assert sol.fib(20) == 6765, "Fallo fib(20)"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   