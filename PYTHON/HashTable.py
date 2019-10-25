class HashTable(object):
    """Docstring for HashTable."""

    def __init__(self, n=100):
        """."""
        self.hash_table = [None] * n
        self.keys = []

    def hash_func(self, key):
        """."""
        return hash(key) % len(self.hash_table)

    def set(self, key, value):
        """."""
        if not self.hash_table[self.hash_func(key)]:
            self.keys.append(key)
            self.hash_table[self.hash_func(key)] = [[key, value]]
        else:
            if key in self.keys:
                for item in self.hash_table[self.hash_func(key)]:
                    if item[0] == key:
                        item[1] = value
                        break
            else:
                self.keys.append(key)
                self.hash_table[self.hash_func(key)].append([key, value])

        return self

    def get(self, key, default=None):
        """."""
        if key not in self.keys or not self.hash_table[self.hash_func(key)]:
            return default

        for item in self.hash_table[self.hash_func(key)]:
            if item[0] == key:
                return item[1]

        return default

    def rem(self, key):
        """."""
        if key not in self.keys or not self.hash_table[self.hash_func(key)]:
            raise KeyError(key)

        if len(self.hash_table[self.hash_func(key)]) == 1:
            self.hash_table[self.hash_func(key)] = None
        else:
            for idx, item in enumerate(self.hash_table[self.hash_func(key)]):
                if item[0] == key:
                    self.hash_table[self.hash_func(key)].pop(idx)
                    break

        for idx, item in enumerate(self.keys):
            if key == item:
                self.keys.pop(idx)

        return self

    def keys(self):
        """."""
        return self.keys

    def items(self):
        """."""
        for key in self:
            yield self

    def __getitem__(self, key):
        """."""
        return self.get(key)

    def __setitem__(self, key, value):
        """."""
        return self.set(key, value)

    def __delitem__(self, key):
        """."""
        return self.rem(key)

    def __len__(self):
        """."""
        return len(self.keys)

    def __str__(self):
        """."""
        return str([i for i in self])

    def __repr__(self):
        """."""
        return str([i for i in self])

    def __iter__(self):
        """."""
        for i in [(key, self.get(key)) for key in self.keys]:
            yield i
