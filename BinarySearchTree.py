from LinkedList import LinkedTree

class BinarySearchTree(LinkedTree):
    '''
    A binary tree implementation using the above linked tree
    '''

    def __init__(self):
        LinkedTree.__init__(self)

    def add(self, variable):
        '''
        Adds a new variable to the tree, in order
        '''
        if self._data is None:
            self._data = variable
        if variable < self._data:
            if self._leftTree is None:
                self.setLeftChild(variable)
            else: self._leftTree.add(variable)
        if variable > self._data:
            if self._rightTree is None:
                self.setRightChild(variable)
            else: self._rightTree.add(variable)

    def addList(self, varList):
        # add item at middle
        # add item at left middle and right middle

        if len(varList) > 1:
            self.add(varList[len(varList)//2])
            self.addList(varList[0 : len(varList)//2])
            self.addList(varList[len(varList)//2 : len(varList)])
        else:
            self.add(varList[0])

    def setRoot(self, newData):
        '''
        sets the root of the given tree with new data
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
            self._leftTree = BinarySearchTree()
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
            self._rightTree = BinarySearchTree()
            self._rightTree._data = newData
        else:
            self._rightTree._data = newData

    def getRoot(self):
        return self._data

    def remove(self, data):
        '''
        removes the specified data from a binary search tree
        '''
        if self.getRoot() == data:
            self.setRoot(self.getRightChild()._getLeftmost())
            self.getRightChild()._removeLeftmost(self.getRightChild()._getLeftmost())
        else:
            self.getLeftChild().remove(data)
            self.getRightChild().remove(data)

    def _removeLeftmost(self):
        '''
        removes the leftmost leaf and returns the value
        '''
        if self.getLeftChild() is None and self.getRightChild() is None:
            return self.getRoot()
        elif self.getLeftChild() is not None:
            print(self.getLeftChild().getRoot())
            self.getLeftChild()._removeLeftmost()
        elif self.getRightChild() is not None:
            self.getRightChild()._removeLeftmost()

    def contains(self, variable):
        '''
        returns true if the tree contains the specified variable
        '''
        print(self._data)
        if self._data == variable:
            return True
        if variable < self._data:
            if self._leftTree is None:
                return False
            else: return self._leftTree.contains(variable)
        if variable > self._data:
            if self._rightTree is None:
                return False
            else: return self._rightTree.contains(variable)
        if self._data is None:
            return False
