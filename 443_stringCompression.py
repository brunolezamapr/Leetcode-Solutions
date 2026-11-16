
class Solution(object):
    def compress(self, chars):
        i = 0
        j = 0

        while j < len(chars):
            s = chars[j]
            count = 0
            while j < len(chars) and chars[j] == s:
                j += 1
                count += 1

            chars[i] = s
            i += 1

            if count > 1:
                for digit in str(count):
                    chars[i] = digit
                    i += 1
        return i

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    # ["a","a","b","b","c","c","c"] → "a2b2c3" → len=6
    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    k = sol.compress(chars)
    assert k == 6 and chars[:k] == ['a', '2', 'b', '2', 'c', '3'], f"Fallo: k={k}, chars[:k]={chars[:k]}"

    # ["a"] → "a" → len=1
    chars = ['a']
    k = sol.compress(chars)
    assert k == 1 and chars[:k] == ['a'], f"Fallo: k={k}"

    # ["a","b","b","b","b","b","b","b","b","b","b","b","b"] → "a12" → len=3
    chars = ['a'] + ['b'] * 12
    k = sol.compress(chars)
    assert k == 3 and chars[:k] == ['a', '1', '2'], f"Fallo: k={k}, chars[:k]={chars[:k]}"

    # ["a","b","c"] sin repetición → "abc" → len=3
    chars = ['a', 'b', 'c']
    k = sol.compress(chars)
    assert k == 3 and chars[:k] == ['a', 'b', 'c'], f"Fallo: k={k}"

    # [] → len=0
    chars = []
    k = sol.compress(chars)
    assert k == 0, f"Fallo: k={k}"

    # ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"] → "a21" → len=3
    chars = ['a'] * 21
    k = sol.compress(chars)
    assert k == 3 and chars[:k] == ['a', '2', '1'], f"Fallo: k={k}, chars[:k]={chars[:k]}"

    # ["a","b","b","c","c","c"] → "a1b2c3" → len=6
    chars = ['a', 'b', 'b', 'c', 'c', 'c']
    k = sol.compress(chars)
    assert k == 6 and chars[:k] == ['a', '1', 'b', '2', 'c', '3'], f"Fallo: k={k}, chars[:k]={chars[:k]}"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   