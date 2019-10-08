"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
"""
##https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def traverse(self):
        node = self # start from the head node
        while node != None:
            print "%s->" % node.val, # access the node value
            node = node.next # move on to the next node

class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     last = 0
    #     head = prev = None
    #     while True:
    #         if l2 is None and l1 is None and last == 0:
    #             break
    #         val = last
    #         if l2 is not None:
    #             val += l2.val
    #             l2 = l2.next
    #         if l1 is not None:
    #             val += l1.val
    #             l1 = l1.next
    #         if val >= 10:
    #             val = val % 10
    #             last = 1
    #         else:
    #             last = 0
    #         current = ListNode(val)
    #         if prev is None:
    #             head = current
    #         else:
    #             prev.next = current
    #         prev = current
    #     return head


    """
    create dummy node as head of the result linked list.
    if any linked list is not iterated to the end, repeat:
        take carry as the init val
        if any linked list is not iterated to the end yet:
            add its value into val
            move (pointer) to the next node
        use the remainder of val as a new node in result,
                append (save) it to result linked list
        move (pointer) to the new node, so next time
                the pointer to new result node can be added to it
        get the carry of current value, which will be the init value when doing
                addition on the next iteration
    once both linked list is iterated, if there is a carry in the last step
        use it as a new node and append to the result linked list

    return the result linked list using the pointer saved in the dummy head node
    """

    def addTwoNumbers(self, l1, l2):
        carry = 0
        # dummy head
        ##to save the linked table
        head = curr = ListNode(0)
        ##repeat as long as any linked list is not iterated to the end:
        while l1 or l2:
            ##take the carry as init value
            val = carry
            ##if any linked list is not iterated to the end, work on it
            if l1:
                ##add its value and mv to the next
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            ##take the remainder as a new node in the result
            curr.next = ListNode(val % 10)
            curr = curr.next
            ##check the possible carry
            carry = val / 10
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next


if __name__ == '__main__':
    s = Solution()

    ##create 2 linked list for 2 nums
    ##num1=243: 3->4->2
    node_1, node_2, node_3=ListNode(2), ListNode(4), ListNode(3)
    node_3.next,node_2.next=node_2,node_1
    ##num2=564: 4->6->5
    node_a, node_b, node_c=ListNode(5), ListNode(6), ListNode(4)
    node_c.next,node_b.next=node_b,node_a

    ##show each linked list and the result
    print node_3.traverse()
    print '+'
    print node_c.traverse()
    print '='
    print s.addTwoNumbers(node_3, node_c).traverse()

