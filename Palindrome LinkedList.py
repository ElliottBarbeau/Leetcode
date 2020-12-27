class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    middle = find_middle(head, head)
    last = reverse_list(middle)
    temp = last
    while head.next:
        if head.value != temp.value:
            return False
        head = head.next
        temp = temp.next

    reverse_list(last) 

    return True

def find_middle(slow, fast):
    slow, fast = slow, fast
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def reverse_list(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev

#2 -> 4 -> 6 -> 4 -> 2

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()