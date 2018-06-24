"""
Exceptions for dict_storage.py.
"""


class DictStorageException(Exception):
    """
    Generic exception for DictStorage.
    """


class KeyAlreadyExists(DictStorageException):
    """
    Trying to save a key that already exists.
    """


class KeyDoesntExist(DictStorageException):
    """
    Trying to load a key that doesn't exist in the storage.
    """
