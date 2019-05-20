import ctypes


class MyArray:
    """
    Implementation of Array in Python.
    """
    def __init__(self, size):
        """
        A method that initializes all parameters.
        """
        assert size > 0
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._items = PyArrayType()
        self.clear(None)

    def __str__(self):
        """
        Converts structure to a string.

        :return: converted structure.
        """
        to_return = "("
        for index in range(self._size - 1):
            to_print = str(self[index])
            to_return = to_return + to_print + ","
        to_print = str(self[self._size - 1])
        return to_return + to_print +")"

    def __len__(self):
        """
        Return length of array.
        :return: 
        """
        return self._size
    
    def __getitem__(self, index):
        """
        Gets the data item with given index.
        Requires: 0 <= index < self.size
        
        :param index: index of the item. 
        :return: the data item with given index.
        """
        return self._items[index]

    def __setitem__(self, index, value):
        """
        Sets the data item with given index.
        Requires: 0 <= index < self.size
        
        :param index: index of the item.
        :param value: value of the item.
        """
        self._items[index] = value

    def clear(self, value):
        """
        A method that changes value of each el\
        into a value (given as parameter).
        """
        for i in range(len(self)):
            self._items[i] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.
        :return: Array Iterator
        """
        return _ArrayIterator(self._elements)

    def isEmpty(self):
        """
        A function that returns whether array is empty.
        :return:
        """
        for item in range(len(self)):
            if self[item] is not None:
                return False
        return True


class _ArrayIterator:
    """
    Helping class to iter Array.
    """
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[ self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration
