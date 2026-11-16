

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

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

def create_cycle(head, pos):
    """Crea un ciclo desde el nodo en índice pos (0-based) hasta el último nodo."""
    if not head or pos < 0:
        return head
    cur = head
    for _ in range(pos):
        cur = cur.next
    last = head
    while last.next:
        last = last.next
    last.next = cur
    return head

def run_tests():
    sol = Solution()

    # [3,2,0,-4] con ciclo en índice 1 → True
    head = create_cycle(build_list([3, 2, 0, -4]), 1)
    assert sol.hasCycle(head) == True, "Fallo: [3,2,0,-4] pos=1"

    # [1,2] con ciclo en índice 0 → True
    head = create_cycle(build_list([1, 2]), 0)
    assert sol.hasCycle(head) == True, "Fallo: [1,2] pos=0"

    # [1] sin ciclo → False
    head = build_list([1])
    assert sol.hasCycle(head) == False, "Fallo: [1] sin ciclo"

    # [1,2,3,4,5] sin ciclo → False
    head = build_list([1, 2, 3, 4, 5])
    assert sol.hasCycle(head) == False, "Fallo: [1,2,3,4,5] sin ciclo"

    # None → False
    assert sol.hasCycle(None) == False, "Fallo: None"

    # [1] con ciclo en índice 0 (self-loop) → True
    head = create_cycle(build_list([1]), 0)
    assert sol.hasCycle(head) == True, "Fallo: [1] pos=0"

    # [1,2,3] con ciclo en índice 2 (último nodo apunta a sí mismo) → True
    head = create_cycle(build_list([1, 2, 3]), 2)
    assert sol.hasCycle(head) == True, "Fallo: [1,2,3] pos=2"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   