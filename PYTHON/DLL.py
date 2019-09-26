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

    def insert_after(self, item_value):
        """Insert one item to the dll."""
        l = LT(item_value=item_value)

        if self.first_item is None:
            self.first_item = l
            self.last_item = l
            self.length += 1
            return

        if self.last_item:
            self.last_item.set_next_item(l)
            l.set_prev_item(self.last_item)
            self.last_item = l
            self.length += 1
            return

    def insert_before(self, item_value):
        """Insert one item to the dll."""
        l = LT(item_value=item_value)

        if self.first_item is None:
            self.first_item = l
            self.last_item = l
            self.length += 1
            return

        if self.first_item:
            self.first_item.set_prev_item(l)
            l.set_next_item(self.first_item)
            self.first_item = l
            self.length += 1
            return

    def remove(self, item):
        """."""
        return

    def print(self):
        """."""
        for item in self:
            print(item)

    def traversal(self, reverse=False):
        """."""
        if not reverse:
            item = self.first_item
            while item is not None:
                yield item
                item = item.get_next_item()
        else:
            item = self.last_item
            while item is not None:
                yield item
                item = item.get_prev_item()

    def __iter__(self):
        """."""
        item = self.first_item
        while item is not None:
            yield item
            item = item.get_next_item()


class LT(object):
    """docstring for LT."""

    def __init__(self, prev_item=None, next_item=None, item_value=None):
        """."""
        self.prev_item = prev_item
        self.next_item = next_item
        self.item_value = item_value

    def __str__(self):
        """."""
        return str(self.item_value)

    def set_prev_item(self, prev_item):
        """."""
        self.prev_item = prev_item

    def set_next_item(self, next_item):
        """."""
        self.next_item = next_item

    def get_prev_item(self):
        """."""
        return self.prev_item

    def get_next_item(self):
        """."""
        return self.next_item
