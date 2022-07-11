from logging import root
import QueueLinkedList as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
rightChild = TreeNode("Cold")
leftChild = TreeNode("Hot")
coffee = TreeNode("Coffee")
tea = TreeNode("Tea")
leftChild.rightChild = coffee
leftChild.leftChild = tea

newBT.leftChild = leftChild
newBT.rightChild = rightChild

# DEPTH FIRST SEARCH


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# preOrderTraversal(newBT)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# inOrderTraversal(newBT)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# postOrderTraversal(newBT)

# BREADTH FIRST SEARCH


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# levelOrderTraversal(newBT)


# SEARCHING BINARY TREE
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "Tree no dey"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                print(root.value.data)
                return "Success"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

# print(searchBT(newBT,'Koko'))

# INSERTING A NODE IN A BINARY TREE
# Use levelOrderTraversal to find a vacant place faster in a short tree


def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully insert at left"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted at right"


fanta = TreeNode("Fanta")
print(insertNode(newBT, fanta))
# levelOrderTraversal(newBT)

# DELETE A NODE FROM A BINARY TREE
# Level Order traversal to get the deepest node


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

        deepestNode = root.value
        return deepestNode


def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is deepestNode:
                root.vale = None
                return
            if root.value.rightChild:
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)


def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "THe BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                deepestNode = getDeepestNode(rootNode)
                root.value.data = deepestNode.data
                deleteDeepestNode(rootNode, deepestNode)
                return "The node has been deleted"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return " Failed to delete"


def deleteBTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

    return "Tree deleted"


deleteBTree(newBT)
levelOrderTraversal(newBT)
