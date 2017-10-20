'''
Copyright : Reese Wells, 2017
'''

from LinkedList import LinkedStack

class Backpack:
    '''
    A backpack data structure

    Components:
        1. Size
            Backpacks have a fixed size
            - this is the max number of items a backpack can contain
            
        2. Compartments
            Backpacks within Backpacks
            - each compartment is smaller than its parent compartment
            - a compartment cannot contain more compartments than its size - 1
            - every compartment has an index

        3. Items
            The data in a Backpack
            - A backpack cannot contain more items than its size
            - The smallest items are always on type, similar to how a student sorts their backpack
    '''

    _compartments = None
    _size = None
    _items = None

    def __init__(self, size = 10):
        '''
        creates a backpack object with a fixed size "size" and a main compartment "main"
        default size is 10
        default compartment is "main"
        '''
        # _compartments is a dictionary
        self._compartments = []
        self._size = size
        self._items = LinkedStack()

    def addCompartment(self, size):
        '''
        adds a compartment with name "name" to the specified parent compartment "compartment"
        the size of the added compartment must be smaller than the parent compartment

        rtype : boolean

        returns true if parent was found and compartment was added
        returns false if parent was not found or parent too small
        '''
        if len(self._compartments) > self._size - 1 or size >= self._size:
            return False
        else:
            self._compartments.append(Backpack(size))
            return True

    def getCompartment(self, index):
        '''
        returns a list of the compartments in the backpack
        '''
        if index < len(self._compartments):
            return self._compartments[index]
        else:
            return None

    def removeCompartment(self, index):
        if index < len(self._compartments):
            self._compartments.remove

    def addItem(self, thing, compartment):
        '''
        attempts to add a new item to the bag

        rtype : boolean

        returns true if the bag had room and the item was added
        returns false if the bag was full
        '''
        if len(self._items) < self._size:
            self._items.append(thing)
            return True
        else:
            return False
