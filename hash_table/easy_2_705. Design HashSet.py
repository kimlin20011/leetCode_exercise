class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.l[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.l[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.l[key]
