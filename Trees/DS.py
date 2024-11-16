class TreeNode:
    def __init__(self, val, left=None, right=None):
        self. val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    #   1
    # l   r

    def add(self, val):
        nd = TreeNode(val)
        if not self.root:
            self.root = nd
        temp = self.root
        while temp:
            if temp.val == val:
                return
            if temp.val > val:
                if not temp.left:
                    temp.left = nd
                    self.count += 1
                    return
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = nd
                    self.count += 1
                    return
                temp = temp.right

    def contains(self, val):
        temp = self.root
        while temp:
            if temp.val == val:
                return True
            temp = temp.left if temp.val > val else temp.right
        return False

    def delete(self, val):
        pass

    def length(self):
        return self.count
