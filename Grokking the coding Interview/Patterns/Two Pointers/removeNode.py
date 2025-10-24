'''
    Link to problem: https://www.educative.io/interview-prep/coding/remove-nth-node-from-end-of-list

    Problem: Remove nth Node from End of List
    Takes 30 mins

    Statement
    Given the head of a singly linked list and an integer n, remove the nth node from the end of the list and return 
    the head of the modified list.

    Constraints:

    The number of nodes in the list is k
    
    1 ≤ k ≤ 10³

    -10³ ≤ Node.Value ≤ 10³

    1 ≤ n ≤ k

    Time Complexity: O(n)
    Space Complexity: O(1)
'''

# Definition for a Linked List node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
#from ds_v1.LinkedList.LinkedList import ListNode

def remove_nth_last_node(head, n):
    #Creates a dummy node to fix incorrect indexes
    dummy = ListNode(val=0)
    #Sets the head node to dummy
    dummy.next = head
    
    #Initialize the first and second pointers and initialze them to the head
    firstPointer = dummy
    secondPointer = dummy
    
    #Moves the firstPointer n steps ahead of the secondPointer
    for _ in range(n):
        firstPointer = firstPointer.next
        
    #Moves the firstPointer and secondPointer until the firstPointer hits the last node
    while firstPointer.next != None:
        firstPointer = firstPointer.next
        secondPointer = secondPointer.next
        
    #Changes the current pointer of the secondPointer to the next two addresses 
    secondPointer.next = secondPointer.next.next
    
    #Eliminates the dummy and return the actual head of the linked list
    return dummy.next

def main():
    #Couldn't test this becasue python has no built in linked list data structure but will work on it in the near future
    #Java and C++ have built in linked list they can be used to test the code otherwise use leetcode or grokking the coding interview

    ...

if __name__ == '__main__':
    main()
