'''

    Explores inorder traversal of Binary Search Tree

    Defines code code of getting a root of a node

    Defines code for getting the right child of a current node

    Code for getting the left child of a current node

'''

class InorderTraversal:
    def __init__(self, tree):
        self.tree = tree

    def rightChild(self, currentNode):
        ...

    def leftChild(self, currentNode):
        ...

    def hasRightChild(self, currentNode):
        ...

    def hasLeftChild(self, currentNode):
        ...


def main():
    inorderTraversal = InorderTraversal([2,4,6,9,3,5])



if __name__ == '__main__':
    main()