'''
    Implementation of the tree data structure

    Methods:
    
    add_child: The add_child method enables the addition of a child to a parent node

    get_level: The get_level method returns the level of a node in the tree

    print_tree: The print_tree method outputs the tree in an intuitive and clear view

    print_subtree_level: This method prints a well descriptive view of the subtree giving the level to output from

    print_subtree_node: This method also outputs the subtree given the node to print from
 
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None


def main():
    ...


if __name__ == '__main__':
    main()