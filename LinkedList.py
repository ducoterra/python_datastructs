'''
Copyright: Reese Wells, 2017
'''

class LinkedQueue:
    '''
    A queue implementation using LinkedLists.
    '''
    _firstNode = None
    _items = 0

    def __init__(self):
        '''
        Creates an empty queue.
        '''
        self._firstNode = None

    def enqueue(self, newData):
        '''
        Adds an item to the back of the queue.
        '''
        newNode = self._Node(newData)
        if self._firstNode is None:
            self._firstNode = newNode
        else:
            currentNode = self._firstNode
            while currentNode._getNextNode() is not None:
                currentNode = currentNode._getNextNode()
            currentNode._setNextNode(newNode)
        self._items = self._items + 1

    def peek(self):
        '''
        Returns the item at the front of the queue but does not dequeue it.
        *Returns None if the queue is empty
        '''
        result = None
        if self._firstNode is not None:
            result = self._firstNode._data
        return result

    def size(self):
        '''
        Returns the number of items in the queue.
        '''
        return self._items

    def dequeue(self):
        '''
        Removes the item at the front of the queue and returns it.
        *Returns None if the queue is empty.
        '''
        result = None
        if self._firstNode is not None:
            result = self._firstNode._getData()
            self._firstNode = self._firstNode._getNextNode()
            self._items = self._items - 1
        return result
    
    def toList(self):
        '''
        Returns a list containing all the items in the queue.
        Returns an empty list if the queue is empty.
        '''
        currentNode = self._firstNode
        result = []
        while currentNode is not None:
            result.append(currentNode._getData())
            currentNode = currentNode._getNextNode()
        return result;

    def toQueue(listicle):
        '''
        Turns a list into a LinkedQueue
        '''
        returnQueue = LinkedQueue()
        for item in listicle:
            returnQueue.enqueue(item)
        return returnQueue

    def clear(self):
        '''
        Removes all objects from the queue.
        '''
        self._firstNode = None;
        self._items = 0

    class _Node:
        _nextNode = None
        _data = None

        def __init__(self, dataInit = None, nextNodeInit = None):
            if nextNodeInit is not None:
                self._nextNode = nextNodeInit
            if dataInit is not None:
                self._data = dataInit

        '''
        returns the Node data
        '''
        def _getData(self):
            return self._data
        
        '''
        returns the next Node
        '''
        def _getNextNode(self):
            return self._nextNode
        
        '''
        sets the data in the specified node
        '''
        def _setData(self, newData = None):
            if newData is None:
                print("newData cannot be null!")
            else:
                self.data = _newData
        
        '''
        sets the next node of the specified node
        '''
        def _setNextNode(self, newNode = None):
            self._nextNode = newNode;

class LinkedStack:
    _top = None
    
    def add(self, newData):
        '''
        adds an element to the top of the stack
        '''
        newNode = self._Node(newData, self._top)
        self._top = newNode
        
    def remove(self):
        '''
        removes the top element from the stack
        '''
        if self._top is not None:
            returnData = self._top._getData()
            self._top = self._top._getNextNode()
            return returnData
        else:
            return None

    def peek(self):
        '''
        returns the top element without removing it
        '''
        if self._top is not None:
            return self._top._getData()
        
    def isEmpty(self):
        '''
        returns true if the stack is empty, false if not
        '''
        return self._top is None
    
    def clear(self):
        '''
        clears all elements from the stack
        '''
        self._top = None
        
    class _Node:
        _nextNode = None
        _data = None

        def __init__(self, dataInit = None, nextNodeInit = None):
            if nextNodeInit is not None:
                self._nextNode = nextNodeInit
            if dataInit is not None:
                self._data = dataInit

        '''
        returns the Node data
        '''
        def _getData(self):
            return self._data
        
        '''
        returns the next Node
        '''
        def _getNextNode(self):
            return self._nextNode
        
        '''
        sets the data in the specified node
        '''
        def _setData(self, newData = None):
            if newData is None:
                print("newData cannot be null!")
            else:
                self.data = _newData
        
        '''
        sets the next node of the specified node
        '''
        def _setNextNode(self, newNode = None):
            self._nextNode = newNode;

class LinkedTree:
    '''
    A tree implementation using LinkedLists.
    '''
    _leftTree = None
    _rightTree = None
    _data = None

    def __init__(self, newData = None):
        '''
        Creates a new empty tree.
        '''
        self._leftTree = None
        self._rightTree = None
        self._data = newData

    def setRoot(self, newData):
        '''
        Sets the root of the given tree

        rtype : boolean

        returns False if unsuccessful
        returns True if successful
        '''
        self._data = newData

    def setLeftChild(self, newData):
        '''
        Sets the left child of the node
        
        rtype : boolean

        returns False if unsuccessful
        returns True if successful
        '''
        if self._leftTree is None:
            self._leftTree = LinkedTree()
            self._leftTree._data = newData
        else:
            self._leftTree._data = newData
        
    def setRightChild(self, newData):
        '''
        Sets the right child of the node
        
        rtype : boolean

        returns False if unsuccessful
        returns True if successful
        '''
        if self._rightTree is None:
            self._rightTree = LinkedTree()
            self._rightTree._data = newData
        else:
            self._rightTree._data = newData

    def getLeftChild(self):
        '''
        Returns the left child, a LinkedTree

        rtype: LinkedTree

        returns None if no child
        '''
        return self._leftTree

    def getRightChild(self):
        '''
        Returns the Right child, a LinkedTree

        rtype: LinkedTree

        returns None if no child
        '''
        return self._rightTree

    def getRoot(self):
        '''
        returns the root of the given tree
        '''
        return self._data

    def clear(self):
        '''
        clears the tree of all children and data
        '''
        self._leftTree = None
        self._rightTree = None
        self._data = None

    def getHeight(self):
        '''
        returns the height of the tree
        '''
        leftHeight = 0
        rightHeight = 0

        if self._leftTree is not None:
            leftHeight = self._leftTree.getHeight()
        if self._rightTree is not None:
            rightHeight = self._rightTree.getHeight()

        return 1 + max(rightHeight, leftHeight)

    def printPreorder(self, depth = 0):
        '''
        prints a formatted version of the tree, preorder
        '''
        append = str(depth) + "_"
        for i in range(0, depth):
            append = append + "_"
            
        print(append + str(self._data))

        if self.getLeftChild() is not None:
            self.getLeftChild().printPreorder(depth + 1)

        if self.getRightChild() is not None:
            self.getRightChild().printPreorder(depth + 1)

    def printPostorder(self, depth = 0):
        '''
        prints a formatted version of the tree, postorder
        '''
        append = str(depth) + "_"
        for i in range(0, depth):
            append = append + "_"
            
        if self.getLeftChild() is not None:
            self.getLeftChild().printPostorder(depth + 1)

        if self.getRightChild() is not None:
            self.getRightChild().printPostorder(depth + 1)

        print(append + str(self._data))

    def printInorder(self, depth = 0):
        '''
        prints a formatted version of the tree, inorder
        '''
        append = str(depth) + "_"
        
        for i in range(0, depth):
            append = append + "_"
            
        if self.getLeftChild() is not None:
            self.getLeftChild().printInorder(depth + 1)

        print(append + str(self._data))

        if self.getRightChild() is not None:
            self.getRightChild().printInorder(depth + 1)

    def printLevelorder(self, depth = 0):
        '''
        prints a formatted version of the tree, levelorder
        '''
        append = str(depth) + "_"

        for i in range(0, self.getHeight() + 1):
            self._printGivenLevel(i,i)
        
    def _printGivenLevel(self, depth, curDepth):
        if self is None:
            return;

        append = str(curDepth) + ""
        for i in range(0,curDepth):
            append = append + "_"
        
        if depth == 1:
            print(append + str(self.getRoot()))
        elif depth > 1:
            if self.getLeftChild() is not None:
                self.getLeftChild()._printGivenLevel(depth - 1, curDepth)
            if self.getRightChild() is not None:
                self.getRightChild()._printGivenLevel(depth - 1, curDepth)
