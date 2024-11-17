from stacks.DS import Stack
from stacks.MinStack import MinStack
from stacks.problems import evaluate_prefix, infix_to_postfix
from Queue.DS import Queue
from Trees.DS import BST
from Trees.alg import top_view, delete, level_order_traversal, postorder


def main():
    bst = BST()
    bst.add(10)
    bst.add(12)
    bst.add(8)
    bst.add(6)
    bst.add(9)
    bst.add(-1)
    bst.add(15)
    bst.add(25)
    bst.add(30)

    tree = delete(bst.root, 10)
    print(level_order_traversal(tree))


if __name__ == '__main__':
    main()
