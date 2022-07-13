class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

# INSERT A NEW NODE
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    # SEARCHING FOR A NODE
    def searchBTree(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"

    # PRE ORDER TRAVERSAL
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        self.inOrderTraversal(index*2+1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
            
    def deleteNode(self, value):
        if self.lastUsedIndex ==0:
            return "There is no node to delete"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                return "The node has been successfully deleted"
            
    def deletBTree(self):
        self.customList = None
        return "The BT has been deleted"

newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffe"))
newBT.preOrderTraversal(1)
print("__________________-------")
newBT.inOrderTraversal(1)
print("__________________-------")
newBT.postOrderTraversal(1)
print("__________________-------")
newBT.levelOrderTraversal(1)
print("__________________-------")

newBT.deleteNode("Cold")
newBT.levelOrderTraversal(1)

newBT.deletBTree()
newBT.levelOrderTraversal(1)
