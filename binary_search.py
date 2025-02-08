class BinarySearchTree(object):
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
    def __str__(self):
        queue = [self]
        values = []
        while queue:
            last = queue.pop(0)
            if last is not None:
                values.append(f"{last.val}")
                queue.append(last.left_child)
                queue.append(last.right_child)
        return ''.join(values)
    def search(self, x):
        if self.val == x:
            return self
        elif x < self.val:
            return self.left_child.search(x)
        elif x > self.val:
            return self.right_child.search(x)
        else:
            return False
    def minimum(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.minimum()
    def maximum(self):
        if self.right_child is None:
            return self
        else:
            return self.right_child.maximum()
    # Create new node
    def insert(self, x):
        if x > self.val:
            if self.right_child is not None:
                self.right_child.insert(x)
            else:
                self.right_child = BinarySearchTree(x)
        else:
            if self.left_child is not None:
                self.left_child.insert(x)
            else:
                self.left_child = BinarySearchTree(x)
        return self
    # Search for node successor
    def next_value(self, x):
        current = self
        successor = None
        while current is not None:
            if current.val > x:
                successor = current
                current = current.left_child
            else:
                current = current.right_child
        return successor
    # Search for node ancestor
    def prev_value(self, x):
        current = self
        successor = None
        while current is not None:
            if current.val < x:
                successor = current
                current = current.right_child
            else:
                current = current.left_child
        return successor
    def delete(self, x):
        parent = self
        node = self
        if not self.search(x):
            return self
        while node.val != x:
            parent = node
            if parent.left_child is not None and x < parent.val:
                node = parent.left_child
            elif parent.right_child is not None and x > parent.val:
                node = parent.right_child
        if node.left_child is None and node.right_child is None:
            if parent.left_child is node:
                parent.left_child = None
            if parent.right_child is node:
                parent.right_child = None
            if parent.value == x:
                return None
        elif node.left_child is None or node.right_child is None:
            if node.left_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.left_child
                elif parent.right_child is node:
                    parent.right_child = node.left_child
            if node.right_child is not None:
                if parent.left_child is node:
                    parent.left_child = node.right_child
                elif parent.right_child is node:
                    parent.right_child = node.right_child
        else:
            next_ = node.next_value(x).val
            node.val = next_
            node.right_child = node.right_child.delete(next_)
        return self
