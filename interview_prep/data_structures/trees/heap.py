import sys


# Arr[(i - 1) / 2] returns its parent
# Arr[(2 * i) + 1] returns its left child
# Arr[(2 * i) + 2] returns its right child

def parent(pos):
    return (pos - 1) // 2


def left_child(pos):
    return (2 * pos) + 1


def right_child(pos):
    return (2 * pos) + 2


class MinHeap:

    def __init__(self):
        self.size = 0
        self.Heap = []

    def is_leaf(self, pos):
        return left_child(pos) >= self.size

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def peek_max(self):
        return self.Heap[0]

    def insert(self, item):
        # insert item to end of heap
        self.Heap.append(item)
        self.size += 1

        # bubble up item as much as necessary
        curr_pos = self.size - 1

        while curr_pos != 0:
            par_pos = parent(curr_pos)
            if self.Heap[par_pos] > self.Heap[curr_pos]:
                self.swap(curr_pos, par_pos)
                curr_pos = par_pos
            else:
                break

    def extract_min(self):
        # extract top node (min) and move last node to this spot
        h_min = self.Heap[0]
        last = self.Heap.pop()
        self.size -= 1
        if self.size > 0:
            self.Heap[0] = last

        # bubble down the top item as much as necessary
        curr_pos = 0

        while left_child(curr_pos) < self.size:
            l_child_pos = left_child(curr_pos)
            r_child_pos = right_child(curr_pos)
            if r_child_pos >= self.size:
                small_child_idx = l_child_pos
            elif self.Heap[l_child_pos] < self.Heap[r_child_pos]:
                small_child_idx = l_child_pos
            else:
                small_child_idx = r_child_pos

            if self.Heap[small_child_idx] < self.Heap[curr_pos]:
                self.swap(curr_pos, small_child_idx)
                curr_pos = small_child_idx
            else:
                break

        return h_min

    def print(self):
        for item in self.Heap:
            print(item)


# Driver Code
if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = MinHeap()
    minHeap.insert(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    # minHeap.print()

    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))

    minHeap.insert(12)
    minHeap.insert(27)
    minHeap.insert(1)
    minHeap.insert(33)
    minHeap.insert(8)

    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))

    minHeap.insert(99)
    minHeap.insert(66)

    print("The Min val is " + str(minHeap.extract_min()))
    print("The Min val is " + str(minHeap.extract_min()))
