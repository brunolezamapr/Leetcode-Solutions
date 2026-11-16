class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n + 1):
            ahead = ahead.next
        
        while ahead:
            behind = behind.next
            ahead = ahead.next
        
        behind.next = behind.next.next
        return dummy.next 

def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def run_tests():
    sol = Solution()
    assert to_list(sol.removeNthFromEnd(build_list([1,2,3,4,5]), 2)) == [1,2,3,5], "Fallo: [1,2,3,4,5] n=2"
    assert to_list(sol.removeNthFromEnd(build_list([1,2]), 1)) == [1], "Fallo: [1,2] n=1"
    assert to_list(sol.removeNthFromEnd(build_list([1]), 1)) == [], "Fallo: [1] n=1"
    assert to_list(sol.removeNthFromEnd(build_list([1,2,3]), 3)) == [2,3], "Fallo: [1,2,3] n=3 (primer nodo)"
    assert to_list(sol.removeNthFromEnd(build_list([1,2,3,4]), 4)) == [2,3,4], "Fallo: [1,2,3,4] n=4 (primer nodo)"
    print("Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    run_tests()
