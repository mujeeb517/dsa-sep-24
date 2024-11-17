from collections import deque, defaultdict

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
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return is_identical(root1.left, root2.left) \
        and is_identical(root1.right, root2.right)


def invert(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)


def level_order_traversal(root):
    if not root:
        return
    q = deque()
    q.append(root)
    res = []

    while q:
        size = len(q)
        items = []
        for _ in range(size):
            nd = q.popleft()
            if nd:
                items.append(nd.val)
                q.append(nd.left)
                q.append(nd.right)
        if items:
            res.append(items)
    return res


def left_view(root):
    levels = level_order_traversal(root)
    for level in levels:
        print(level[0], end=' ')


def spiral_order(root):
    if not root:
        return
    q = deque()
    q.append(root)
    ltr = True

    while q:
        size = len(q)
        items = []
        for _ in range(size):
            nd = q.popleft()
            if nd:
                items.append(nd.val)
                q.append(nd.left)
                q.append(nd.right)

        if not ltr:
            items.reverse()
        ltr = not ltr
        print(items)


def spiral_order2(root):
    levels = level_order_traversal(root)
    ltr = True
    for level in levels:
        if not ltr:
            level.reverse()
        print(level)
        ltr = not ltr


def vertical_order(root):
    res = defaultdict(list)
    if not root:
        return res
    q = deque()
    q.append((root, 0))

    while q:
        nd, level = q.popleft()
        if nd:
            res[level].append(nd.val)
            q.append((nd.left, level-1))
            q.append((nd.right, level+1))
    levels = []
    for item in sorted(res.items()):
        levels.append(item[1])
    return levels


def top_view(root):
    if not root:
        return
    q = deque()
    res = {}
    q.append((root, 0))

    while q:
        nd, hd = q.popleft()
        if nd:
            if not hd in res:
                res[hd] = nd.val
            q.append((nd.left, hd-1))
            q.append((nd.right, hd+1))

    return sorted(res.items())


def delete(root, val):
    if not root:
        return None
    if root.val > val:
        return delete(root.left, val)
    if root.val < val:
        return delete(root.right, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.right
        else:
            min_val = find_min(root.right)
            root.val = min_val
            root.right = delete(root.right, min_val)

    return root
