import random

class RandomizedSet:

    def __init__(self):
        self.values = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.values:
            return False  # Element already exists, no need to insert

        self.values.add(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.values:
            return False  # Element not present, nothing to remove

        self.values.remove(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return random.choice(list(self.values))
