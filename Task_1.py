from __future__ import annotations


class Node:
    data: int
    next: Node | None

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class LinkedList:
    head: Node | None

    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def reverse(self) -> None:
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def insertion_sort(self) -> None:
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next

            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head

                while search.next and search.next.data < current.data:
                    search = search.next

                current.next = search.next
                search.next = current

            current = next_node

        self.head = sorted_head

    def print_list(self) -> None:
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


def merge_sorted_lists(
    first_list: LinkedList,
    second_list: LinkedList
) -> LinkedList:
    merged_list = LinkedList()
    dummy = Node(0)
    tail = dummy

    first = first_list.head
    second = second_list.head

    while first and second:
        if first.data <= second.data:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next

        tail = tail.next

    if first:
        tail.next = first
    else:
        tail.next = second

    merged_list.head = dummy.next

    return merged_list


if __name__ == "__main__":
    first_list = LinkedList()

    first_list.insert_at_end(5)
    first_list.insert_at_end(1)
    first_list.insert_at_end(8)
    first_list.insert_at_end(3)

    print("Початковий список:")
    first_list.print_list()

    first_list.reverse()

    print("\nРеверсований список:")
    first_list.print_list()

    first_list.insertion_sort()

    print("\nВідсортований перший список:")
    first_list.print_list()

    second_list = LinkedList()

    second_list.insert_at_end(7)
    second_list.insert_at_end(2)
    second_list.insert_at_end(6)
    second_list.insert_at_end(4)

    second_list.insertion_sort()

    print("\nВідсортований другий список:")
    second_list.print_list()

    merged_list = merge_sorted_lists(first_list, second_list)

    print("\nОб'єднаний відсортований список:")
    merged_list.print_list()