
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def search(root, data):
    # Base Cases: root is null or data is present at root
    if root is None or root.data == data:
        return root

    # data is greater than root's data
    if root.data < data:
        return search(root.right, data)

    # data is smaller than root's data
    return search(root.left, data)


def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


def morris_traversal(root):
    """Generator function for
      iterative inorder tree traversal"""

    current = root

    while current is not None:

        if current.left is None:
            yield current.data
            current = current.right
        else:

            # Find the inorder
            # predecessor of current
            pre = current.left
            while pre.right is not None and pre.right is not current:
                pre = pre.right

            if pre.right is None:

                # Make current as right
                # child of its inorder predecessor
                pre.right = current
                current = current.left

            else:
                # Revert the changes made
                # in the 'if' part to restore the
                # original tree. i.e., fix
                # the right child of predecessor
                pre.right = None
                yield current.data
                current = current.right


def min_value_node(node):
    current = node

    # loop down to find the leftmost leaf of right subtree
    # or if implemented differently could be rightmost leaf of left subtree
    while current.left is not None:
        current = current.left

    return current


def delete_node(root, data):

    # Base Case
    if root is None:
        return root

    # If smaller than the root's
    if data < root.data:
        root.left = delete_node(root.left, data)

    # If greater than the root's
    elif data > root.data:
        root.right = delete_node(root.right, data)

    # If same as root's key, then node to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        # A different solution: Get the inorder predecessor (biggest in the left subtree)
        temp = min_value_node(root.right)

        # Copy the inorder successor's content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.data)

    return root


# run main
def main():
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Print stuff
    inorder(r)
    print('----------')
    preorder(r)
    print('----------')
    postorder(r)
    print('----------')
    for item in morris_traversal(r):
        print(item)

    return


if __name__ == '__main__':
    main()
