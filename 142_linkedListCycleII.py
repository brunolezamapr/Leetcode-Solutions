

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        curr = head
        while curr != slow:
            curr = curr.next
            slow = slow.next

        return curr

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
    """Devuelve (head, entry_node) donde entry_node es el nodo en índice pos."""
    if not head or pos < 0:
        return head, None
    cur = head
    for _ in range(pos):
        cur = cur.next
    last = head
    while last.next:
        last = last.next
    last.next = cur
    return head, cur

def run_tests():
    sol = Solution()

    # [3,2,0,-4] ciclo en índice 1 → devuelve el nodo con val=2
    head, entry = create_cycle(build_list([3, 2, 0, -4]), 1)
    assert sol.detectCycle(head) is entry, "Fallo: [3,2,0,-4] pos=1"

    # [1,2] ciclo en índice 0 → devuelve el nodo con val=1
    head, entry = create_cycle(build_list([1, 2]), 0)
    assert sol.detectCycle(head) is entry, "Fallo: [1,2] pos=0"

    # [1] sin ciclo → None
    head = build_list([1])
    assert sol.detectCycle(head) is None, "Fallo: [1] sin ciclo"

    # [1,2,3,4,5] sin ciclo → None
    head = build_list([1, 2, 3, 4, 5])
    assert sol.detectCycle(head) is None, "Fallo: [1,2,3,4,5] sin ciclo"

    # None → None
    assert sol.detectCycle(None) is None, "Fallo: None"

    # [1] self-loop en índice 0 → devuelve el nodo con val=1
    head, entry = create_cycle(build_list([1]), 0)
    assert sol.detectCycle(head) is entry, "Fallo: [1] pos=0"

    # [1,2,3] ciclo en índice 2 → devuelve el nodo con val=3
    head, entry = create_cycle(build_list([1, 2, 3]), 2)
    assert sol.detectCycle(head) is entry, "Fallo: [1,2,3] pos=2"

    # [1,2,3,4,5,6] ciclo en índice 3 → devuelve el nodo con val=4
    head, entry = create_cycle(build_list([1, 2, 3, 4, 5, 6]), 3)
    assert sol.detectCycle(head) is entry, "Fallo: [1,2,3,4,5,6] pos=3"

    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()   