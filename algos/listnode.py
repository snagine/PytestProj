class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class NodeOps:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        next_node = head.next
        curr_node = head
        if not head:
            return head
        while next_node != None:
            if curr_node.val == next_node.val:
                curr_node.next = next_node.next
                next_node = next_node.next
            else:
                next_node = next_node.next
                curr_node = curr_node.next
        return head
        # if head == None:
        #     return head
        #
        # current = head.next
        # prev = head
        #
        # while current != None:
        #     if current.val == prev.val:
        #         prev.next = current.next
        #         current = current.next
        #     else:
        #         current = current.next
        #         prev = prev.next
        #
        # return head

    def middleNode(self, head: ListNode) -> ListNode:
        middle = head
        end = head

        while middle.next and end.next:
            middle = middle.next
            end = end.next.next
        return middle


one = ListNode(1)
two = ListNode(1)
three = ListNode(1)
four = ListNode(4)
five = ListNode(4)
six = ListNode(6)
seven = ListNode(7)
eight = ListNode(7)
nine = ListNode(9)

head = one
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine


# print(one.val, one.next.val, two.next.val)
# mid = NodeOps().middleNode(head)
# print(mid.val)

deduped = NodeOps().deleteDuplicates(head)
print(deduped.val, deduped.next.val, deduped.next.next.val)
