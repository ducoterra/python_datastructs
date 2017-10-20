'''
Copyright Reese Wells, 2017
'''
import BinarySearchTree

class PrefixTree:
    '''
    A prefix tree implementation
    '''
    
    def __init__(self):
        '''
        creates an empty prefix tree
        '''
        self._children = None
        self._data = False
        self._END = 256

    def _initChildren(self):
        '''
        initiates 256 children to false prefix trees, with one extra
        boolean to signify the end of a word

        rtype : boolean

        returns true if successful in initializing all the children
        '''
        t1 = []
        for i in range(0, 256):
            t1.append(PrefixTree())

        t1.append(False)
        self._children = t1

    def add(self, letter):
        '''
        Adds a new letter to the tree

        rtype : boolean

        returns True if data was added
        returns False if data was already there
        '''
        if self._children is None:
            self._initChildren()
        if not self._children[ord(letter)]._data:
            self._children[ord(letter)]._data = True

    def contains(self, letter):
        '''
        Checks if the given node has a child that matches data

        rtype : boolean

        returns True if one of the children's data matches
        returns False if none of the children's data matches
        '''
        if self._children[ord(letter)]._data:
            return True
        return False

    def addWord(self, word):
        '''
        adds a word to the tree by recursively calling add()

        rtype : boolean

        returns True if the word was added
        returns False if the tree already contained the word

        NOTE: returns true if given an empty string
        '''
        if len(word) == 0:
            if self._children is None:
                self._initChildren()
            self._children[self._END] = True
        else:
            self.add(word[:1])
            self._children[ord(word[:1])].addWord(word[1:])

    def containsWord(self, word):
        '''
        Checks if the tree contains the given word by calling contains()
        recursively and checking each letter

        rtype : boolean

        returns True if the tree contains the word
        returns False if the tree does not contain the word
        '''
        if len(word) == 0:
            return self._children[self._END]
        elif self._children is not None and self._children[ord(word[:1])]._data:
            return self._children[ord(word[:1])].containsWord(word[1:])
        else:
            return False

def test():
    # test making the tree
    p = PrefixTree()
    print ("adding 'a': " + str(p.add('a')))
    print ("adding 'b': " + str(p.add('b')))
    print ("adding 'a': " + str(p.add('a')))
    print ("contains 'a': " + str(p.contains('a')))

    # test containsWord
    print ("p.containsWord('aa'): " + str(p.containsWord('aa')))
    print ("p.containsWord('ab'): " + str(p.containsWord('ab')))
    print ("p.containsWord('abcd'): " + str(p.containsWord('abcd')))
    print ("p.containsWord('d'): " + str(p.containsWord('d')))

    # test addWord
    print ("p = PrefixTree(): ")
    p = PrefixTree()
    print ("adding 'hello': " + str(p.addWord('hello')))
    print ("adding 'hello': " + str(p.addWord('hello')))
    print ("adding 'world': " + str(p.addWord('world')))
    print ("adding 'python': " + str(p.addWord('python')))
    print ("adding 'java': " + str(p.addWord('java')))
    print ("adding 'word': " + str(p.addWord('word')))

    # test containsWord
    print ("p.containsWord('hello'): " + str(p.containsWord('hello')))
    print ("p.containsWord('hel'): " + str(p.containsWord('hel')))
    print ("p.containsWord('world'): " + str(p.containsWord('world')))
    print ("p.containsWord('w'): " + str(p.containsWord('w')))
    print ("p.containsWord('python'): " + str(p.containsWord('python')))
    print ("p.containsWord('pythone'): " + str(p.containsWord('pythone')))
    print ("p.containsWord('java'): " + str(p.containsWord('java')))
    print ("p.containsWord(''): " + str(p.containsWord('')))
    print ("p.containsWord('word'): " + str(p.containsWord('word')))

    return p

def testDictionary():
    '''
    Adds all the words in the dictionary from the file "words.txt"
    
    rtype : PrefixTree()
    '''
    dictionary = open("words.txt", 'r')
    dictionaryTree = PrefixTree()

    # first lets get a line count to know how many words we've added at any give time
    lineCount = 0
    for line in dictionary:
        lineCount = lineCount + 1

    # now let's add the words, spitting out percentages on occasion
    currentLine = 0
    currentProgress = 0
    dictionary = open("words.txt", 'r')

    for line in dictionary:

        # get our current progress through the words
        percentDone = int((currentLine / lineCount) * 100)
        if percentDone > currentProgress:
            currentProgress = percentDone
            print("finished adding " + str(currentProgress) + "% of words in the dictionary")

        # add the next word
        dictionaryTree.addWord(line.strip())

        #increment currentLine
        currentLine = currentLine + 1

    return dictionaryTree

# dictionary = testDictionary()













    
