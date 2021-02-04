from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_alternate_k_elements(head, k):
    reverse = True

    current, previous = head, None

    while current:

        node_before_sublist = previous
        last_node_of_post_reversal_sublist = current

        i = 0
        if reverse:
            next = None
            while current and i < k:
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1

            if node_before_sublist:
                node_before_sublist.next = previous
            else:
                head = previous

            last_node_of_post_reversal_sublist.next = current
            reverse = False

        else:
            while current and i < k:
                previous = current
                current = current.next
                i += 1
            reverse = True

    previous = last_node_of_post_reversal_sublist
        
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
