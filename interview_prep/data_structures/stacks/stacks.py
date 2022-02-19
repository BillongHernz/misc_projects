class StackArr:
    def __init__(self):
        self.stack = []
        self.size_stack = 0

    def push(self, val):
        self.size_stack += 1
        self.stack.append(val)

    def pop(self):
        self.size_stack -= 1
        return self.stack.pop()

    def peek(self):
        if self.size_stack > 0:
            return self.stack[-1]
        return None

    def empty(self):
        return self.size_stack == 0

    def size(self):
        return self.size_stack


from collections import deque


class StackDeq:
    def __init__(self):
        self.stack = deque()
        self.size_stack = 0

    def push(self, val):
        self.size_stack += 1
        self.stack.append(val)

    def pop(self):
        self.size_stack -= 1
        return self.stack.pop()

    def peek(self):
        if self.size_stack > 0:
            return self.stack[-1]
        return None

    def empty(self):
        return self.size_stack == 0

    def size(self):
        return self.size_stack


def test_stack(stack):
    print(' Size : isempty')
    print('--- ' + str(stack.size()) + ' : ' + str(stack.empty()))
    stack.push('a')
    print(stack.peek())
    stack.push('b')
    print(stack.peek())
    stack.push('c')
    print(stack.peek())

    print(' Size : isempty')
    print('--- ' + str(stack.size()) + ' : ' + str(stack.empty()))
    print('\nElements popped from stack:')
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())

    print(' Size : isempty')
    print('--- ' + str(stack.size()) + ' : ' + str(stack.empty()))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackLL:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    # Get the current size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value



def main():
    stack = StackArr()
    stack = StackDeq()
    stack = StackLL()
    test_stack(stack)


if __name__ == '__main__':
    main()
