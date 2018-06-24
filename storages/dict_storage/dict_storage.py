"""
Basic storage that uses a dictionary.
"""
from core.base_storage import BaseStorage
from storages.dict_storage.exceptions import KeyAlreadyExists, KeyDoesntExist


class DictStorage(BaseStorage):
    """
    Basic storage that uses a dictionary.
    """

    def __init__(self):
        self._internal_dict = {}

    def save(self, key, value, override=False):
        """
        Save a value with a given key in the dict.
        """
        if key in self._internal_dict and not override:
            raise KeyAlreadyExists("Key ({}) already exists the the flag override==False")

        self._internal_dict[key] = value

    def load(self, key):
        """
        Loads the value with of the given key.
        """
        value = self._internal_dict.get(key)
        if not value:
            raise KeyDoesntExist("Key ({}) doesn't exist in the storage")

        return value

    def delete(self, key):
        """
        Deletes the value with the given key.
        """
        if key not in self._internal_dict:
            KeyDoesntExist("Key ({}) doesn't exist in the storage")

        del self._internal_dict[key]
