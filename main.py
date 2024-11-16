from stacks.DS import Stack
from stacks.MinStack import MinStack
from stacks.problems import evaluate_prefix, infix_to_postfix
from Queue.DS import Queue
from Trees.DS import BST
from Trees.alg import preorder, inorder, postorder, find_min, height


def main():
    bst = BST()
    bst.add(10)
    bst.add(12)
    bst.add(8)
    bst.add(6)
    bst.add(9)
    bst.add(-1)

    print(find_min(bst.root))
    print(height(bst.root))

if __name__ == '__main__':
    main()
