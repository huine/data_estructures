class DLL(object):
    """docstring for dll."""

    def __init__(self):
        """."""
        self.last_item = None
        self.first_item = None
        self.length = 0

    def __len__(self):
        """."""
        return self.length

    def is_empty(self):
        """."""
        return not self.length and True or False

    def insert_after(self, value):
        """Insert one item to the dll."""
        l = LT(value=value)

        if self.first_item is None:
            self.first_item = l
            self.last_item = l
            self.length += 1
            return

        if self.last_item:
            self.last_item.next_item = l
            l.prev_item = self.last_item
            self.last_item = l
            self.length += 1
            return

    def insert_before(self, value):
        """Insert one item to the dll."""
        l = LT(value=value)

        if self.first_item is None:
            self.first_item = l
            self.last_item = l
            self.length += 1
            return

        if self.first_item:
            self.first_item.prev_item = l
            l.next_item = self.first_item
            self.first_item = l
            self.length += 1
            return

    def remove(self, value):
        """."""
        r = None
        if self.first_item.value == value:
            r = self.first_item.value
            self.first_item.next_item.prev_item = None
            self.first_item = self.first_item.next_item
            self.length -= 1
            return r

        if self.last_item.value == value:
            r = self.last_item.value
            self.last_item.prev_item.next_item = None
            self.last_item = self.last_item.prev_item
            self.length -= 1
            return r

        for item in self:
            if item.value == value:
                item.prev_item.next_item = item.next_item
                item.next_item.prev_item = item.prev_item
                r = item.value
                del item
                self.length -= 1

                return r
        return r

    def pop(self, key):
        """."""
        curr = self[key]
        self.remove(curr.value)
        return curr

    def traversal(self, reverse=False):
        """."""
        if not reverse:
            item = self.first_item
            while item is not None:
                yield item.value
                item = item.next_item
        else:
            item = self.last_item
            while item is not None:
                yield item.value
                item = item.prev_item

    def has_item(self, value):
        """."""
        for item in self:
            if item.value == value:
                return True
        return False

    def __iter__(self):
        """."""
        item = self.first_item
        while item is not None:
            yield item
            item = item.next_item

    def __getitem__(self, key):
        """."""
        assert(isinstance(key, int))

        if key < 0:
            key = key + 1

        if self.is_empty() or not abs(key) < self.length:
            return None

        if key == 0:
            return self.first_item

        if key == self.length - 1:
            return self.last_item

        if key >= 1:
            curr = self.first_item
            for i in range(key):
                curr = curr.next_item
        else:
            curr = self.last_item
            for i in range(abs(key)):
                curr = curr.prev_item

        return curr


class LT(object):
    """docstring for LT."""

    def __init__(self, prev_item=None, next_item=None, value=None):
        """."""
        self.prev_item = prev_item
        self.next_item = next_item
        self.value = value

    def __str__(self):
        """."""
        return str(self.value)

    def __repr__(self):
        """."""
        return str(self.value)
