from DLL import DLL
class HashTable(object):
    """Docstring for HashTable."""

    def __init__(self):
        """."""
        self.__attr_list__ = DLL()

    def put(self, key, value):
        if self.__attr_list__.has_item(key):
            self.delete(key)
        self.__attr_list__.insert_after(key)

        key_hash = str(hash(key))
        setattr(self, key_hash, value)
        return True

    def get(self, key, default=None):
        key = str(hash(key))
        return getattr(self, key, default)

    def delete(self, key):
        r = self.get(key)
        self.__attr_list__.remove(key)
        key = str(hash(key))
        delattr(self, key)
        return r

    def __iter__(self):
        """."""
        for key in self.__attr_list__:
            yield (key.value, self.get(key.value))
