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


def reverse_sub_list(head, p, q):
    

    current, previous = head, None
    i = 0
    while current and i < p - 1:
        previous = current
        current = current.next
        i += 1

    node_before_list = previous
    last_node_of_sublist = current

    i = 0
    while i <= q - p:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    if node_before_list:
        node_before_list.next = previous
    else:
        head = previous

    last_node_of_sublist.next = current

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
