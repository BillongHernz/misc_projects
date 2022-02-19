
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self, root):
        self.root = root


def print_linked_list(linked_list):

    curr = linked_list.root
    while curr:
        print(curr.data)
        curr = curr.next


def insert_start_linked_list(linked_list, data):
    temp = linked_list.root
    linked_list.root = Node(data)
    linked_list.root.next = temp


def insert_end_linked_list(linked_list, data):
    curr = linked_list.root
    while curr and curr.next:
        curr = curr.next
    if curr:
        curr.next = Node(data)


def search_linked_list(linked_list, val):
    curr = linked_list.root
    while curr and curr.data != val:
        curr = curr.next


def main():

    return


if __name__ == '__main__':
    main()
