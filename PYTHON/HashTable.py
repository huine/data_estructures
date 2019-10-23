class HashTable(object):
    """Docstring for HashTable."""

    def __init__(self, n=100):
        """."""
        self.hash_table = [None] * n

    def hash_func(self, key):
        """."""
        return hash(key) % len(self.hash_table)

    def set(self, key, value):
        """."""
        self.hash_table[self.hash_func(key)] = (key, value)
        return self

    def get(self, key, default=None):
        """."""
        return self.hash_table[self.hash_func(key)] and\
            self.hash_table[self.hash_func(key)][1] or default

    def rem(self, key):
        """."""
        self.hash_table[self.hash_func(key)] = None
        return self

    def keys(self):
        """."""
        return [k for k, v in self]

    def items(self):
        """."""
        for item in self:
            yield item

    def __getitem__(self, key):
        """."""
        return self.get(key)

    def __setitem__(self, key, value):
        """."""
        return self.set(key, value)

    def __len__(self):
        """."""
        return len([i for i in self.hash_table if i is not None])

    def __str__(self):
        """."""
        return str([i for i in self.hash_table if i is not None])

    def __repr__(self):
        """."""
        return str([i for i in self.hash_table if i is not None])

    def __iter__(self):
        """."""
        for i in [i for i in self.hash_table if i is not None]:
            yield i
