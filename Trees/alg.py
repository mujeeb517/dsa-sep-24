# Root Left Right
def preorder(root):
    if not root:
        return
    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)
# Left Root Right


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)
# Left Right Root


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')


def find_min(root):
    if not root:
        return None
    if not root.left:
        return root.val
    return find_min(root.left)


def height(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)


def isBalanced(root):
    if not root:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    return abs(left_height-right_height) <= 1 and \
        isBalanced(root.left) \
        and isBalanced(root.right)


def count_leaves(root):
    if not root:
        return 0
    if not root.right and not root.left:
        return 1
    if not root.left and root.right:
        return 0
    
    return count_leaves(root.left)+count_leaves(root.right)


def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if root1.val != root2.val:
        return False
    return is_identical(root1.left, root2.left) \
        and is_identical(root1.right, root2.right)
