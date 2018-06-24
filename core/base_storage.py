"""
Includes a base class for storage classes.
"""
import abc


class BaseStorage(metaclass=abc.ABCMeta):
    """
    Base class for storages to implement.
    """

    @abc.abstractmethod
    def save(self, value):
        """
        Saves a value in the storage.
        @param value: Any value that should be saved in the storage.
        @type value: C{object}
        """
        pass

    @abc.abstractmethod
    def load(self, key):
        """
        Loads a value from the storage using a key.
        @param key: Something that indicates the value to load from the storage.
        @type key: C{object}
        @return: The loaded value.
        @rtype: C{object}
        """
        pass

    @abc.abstractmethod
    def delete(self, key):
        """
        Deletes a value from the storage using a key.
        @param key: Something that indicates the value to delete from the storage.
        @type key: C{object}
        """
        pass
