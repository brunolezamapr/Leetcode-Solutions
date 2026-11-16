
class Solution(object):
    def maxVowels(self, s, k):
        vowels = 'aeiou'
        vowels_count = sum(1 for letter in s[:k] if letter in vowels)
        vowels_max = vowels_count

        for i in range(k, len(s)):
            if s[i] in vowels:
                vowels_count += 1
            if s[i - k] in vowels:
                vowels_count -= 1
            if vowels_count > vowels_max:
                vowels_max = vowels_count

        return vowels_max

# --- PRUEBAS ---

def run_tests():
    sol = Solution()

    assert sol.maxVowels("abciiidef", 3) == 3, "Fallo 'abciiidef' k=3"
    assert sol.maxVowels("aeiou", 2) == 2, "Fallo 'aeiou' k=2"
    assert sol.maxVowels("leetcode", 3) == 2, "Fallo 'leetcode' k=3"
    assert sol.maxVowels("a", 1) == 1, "Fallo 'a' k=1"
    assert sol.maxVowels("b", 1) == 0, "Fallo 'b' k=1"
    assert sol.maxVowels("abc", 3) == 1, "Fallo 'abc' k=3"
    assert sol.maxVowels("aeiou", 5) == 5, "Fallo 'aeiou' k=5"
    assert sol.maxVowels("abcde", 1) == 1, "Fallo 'abcde' k=1"
    assert sol.maxVowels("brrd", 2) == 0, "Fallo 'brrd' k=2"
    assert sol.maxVowels("aa", 1) == 1, "Fallo 'aa' k=1"
    assert sol.maxVowels("aeiou", 1) == 1, "Fallo 'aeiou' k=1"
    assert sol.maxVowels("abciiidef", 1) == 1, "Fallo 'abciiidef' k=1"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   