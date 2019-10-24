class AVLTree(object):
    """Docstring for ACLTree."""

    def __init__(self):
        """."""
        self.root = None

    def __str__(self):
        """."""
        if self.root is None:
            return '<empty>'
        return str(self.root)

    def height(self, node):
        """."""
        if node is None:
            return -1
        return node.height

    def update_height(self, node):
        """."""
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rebalance(self, node):
        """."""
        while node is not None:
            self.update_height(node)
            node = node.parent

    def insert(self, val):
        """."""
        new_node = AVLNode(val)
        if self.root is None:
            self.root = new_node
            return

        self.root.insert(new_node)
        self.rebalance(new_node)

    def find_min_sub(self):
        """."""
        return self.root and self.root.find_min_sub()

    def find_min(self):
        """."""
        node = self.root
        while node is not None:
            if node.left is None:
                return node
            else:
                node = node.left
        return node

    def find_max(self):
        """."""
        node = self.root
        while node is not None:
            if node.right is None:
                return node
            else:
                node = node.right
        return node

    def find(self, val):
        """."""
        node = self.root
        while node is not None:
            if node == val:
                return node
            elif val < node:
                node = node.left
            else:
                node = node.right
        return node


class AVLNode(object):
    """Docstring for AVLNode."""

    def __init__(self, value):
        """."""
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.height = -1

    def _str(self):
        """Internal method for ASCII art."""
        label = '%s(%s-%s)' % (str(self.value), str(self.height),
                               str(abs(getattr(self.left, 'height', -1) - getattr(self.right, 'height', -1))))
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.':
            label = ' ' + label[1:]
        if label[-1] == '.':
            label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle - 2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
            [left_line + ' ' * (width - left_width - right_width) + right_line
             for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        """."""
        return '\n'.join(self._str()[0])

    # def __str__(self):
    #     """."""
    #     return str({'value': self.value, 'height': self.height})

    def __lt__(self, other):
        """."""
        if isinstance(other, AVLNode):
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        """."""
        if isinstance(other, AVLNode):
            return self.value > other.value
        else:
            return self.value > other

    def __eq__(self, other):
        """."""
        if isinstance(other, AVLNode):
            return self.value == other.value
        else:
            return self.value == other

    def insert(self, node):
        """."""
        if node is None:
            return

        if node < self:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)
        return

    def find_min_sub(self):
        """."""
        node = self
        if node.left is not None:
            node = node.left

        return node
