class Node:

    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self,val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,val):
        self.nextNode = val

class LinkedList:

    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size+=1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.getData())
            curr = curr.getNextNode()

    def searchNode(self,data):
        curr = self.head
        found = False

        while curr and found is False:
            if curr.getData == data:
                print("data found")
                found = True
        return True

myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())
print(myList.searchNode(15))
print("H")
