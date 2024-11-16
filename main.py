from stacks.DS import Stack
from stacks.MinStack import MinStack
from stacks.problems import evaluate_prefix, infix_to_postfix
from Queue.DS import Queue


def main():
    q = Queue()
    print(q.length())

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(q.peek())

    while not q.is_empty():
        print(q.dequeue())



if __name__ == '__main__':
    main()
