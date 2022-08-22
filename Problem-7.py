'''
Problem 7
0.0/20.0 points (graded)
Implement the class myDict with the methods below, which will represent a dictionary without using a dictionary object. The methods you implement below should have the same behavior as a dict object, including raising appropriate exceptions. Your code does not have to be efficient. Any code that uses a Python dictionary object will receive 0.

For example:

With a dict:       With a myDict:
-------------------------------------------------------------------------------
d = {}             md = myDict()        # initialize a new object using 
                                          your choice of implementation

d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair

print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1

del(d[1])          md.delete(1)         # use delete method to remove 
                                          key,value pair associated with key 1
class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        #FILL THIS IN
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        #FILL THIS IN
        
    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN
        
    def delete(self, k):
        """ k, immutable object """   
        #FILL THIS IN
    
Paste your entire class in the box below. Do not leave any print statements.
'''
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def _init_(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """

        self.vals = {}
    
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """

        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    
    def _str_(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """

        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """

        if e not in self.vals:
            return 0
        else:
            return self.vals[e]

    def _add_(self, other):
        """ assumes other is a Bag instance
            Returns dictionary of combined values between two Bag instances. """

        combinedBag = Bag()
        combinedBag.vals = self.vals.copy()
        for e in other.vals:
            for i in range(other.vals[e]):
                combinedBag.insert(e)
        return combinedBag

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals:
            del self.vals[e]    
        else:
            None

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return e in self.vals