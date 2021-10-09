class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data: MutableMapping[int, int] = {}
        self._data_list: MutableSequence[int] = []
        

    # Set dictionary[val] = length of the list, and append val to the list. The order is important.
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._data:
            return False
        self._data[val] = len(self._data_list)
        self._data_list.append(val)
        return True
        

    # Let index = index of 'val' in the list and let the last element of the list be 'last'. 
    # Set list[index] = last.
    # Set dictionary[last] = index.
    # Delete dictionary[val].
    # Delete 'last' from the list.
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._data:
            return False
        index = self._data[val]
        last = self._data_list[-1]
        self._data_list[index] = last
        self._data[last] = index
        del self._data[val]
        self._data_list.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self._data_list)
