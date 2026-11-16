
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# --- PRUEBAS ---

def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for v in arr[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def run_tests():
    sol = Solution()

    # [1,2,3,4,5] → nodo 3 (índice 2)
    head = build_list([1, 2, 3, 4, 5])
    assert sol.middleNode(head).val == 3, "Fallo [1,2,3,4,5]"

    # [1,2,3,4,5,6] → nodo 4 (índice 3, segundo medio)
    head = build_list([1, 2, 3, 4, 5, 6])
    assert sol.middleNode(head).val == 4, "Fallo [1,2,3,4,5,6]"

    # [1] → nodo 1
    head = build_list([1])
    assert sol.middleNode(head).val == 1, "Fallo [1]"

    # [1,2] → nodo 2 (segundo medio)
    head = build_list([1, 2])
    assert sol.middleNode(head).val == 2, "Fallo [1,2]"

    # [1,2,3] → nodo 2
    head = build_list([1, 2, 3])
    assert sol.middleNode(head).val == 2, "Fallo [1,2,3]"

    # [1,2,3,4] → nodo 3 (segundo medio)
    head = build_list([1, 2, 3, 4])
    assert sol.middleNode(head).val == 3, "Fallo [1,2,3,4]"

    # [7,8,9,10,11,12,13] → nodo 10
    head = build_list([7, 8, 9, 10, 11, 12, 13])
    assert sol.middleNode(head).val == 10, "Fallo [7..13]"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   