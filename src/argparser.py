import argparse

from algos.factorial import factorial, factorial_recursive
from algos.fibonacci import fibo, fibo_recursive
from sorts import run_sort
from structs.stack_list import StackList
from structs.queue_list import QueueList

_stack_instance: StackList|None=None
_queue_instance: QueueList|None=None

def _handle_fact(ns):
    return factorial(ns.n)
def _handle_factr(ns):
    return factorial_recursive(ns.n)
def _handle_fib(ns):
    return fibo(ns.n)
def _handle_fibr(ns):
    return fibo_recursive(ns.n)
def _handle_sort(ns):
    return run_sort(ns.algo, ns.nums)
def _handle_stack(ns):
    global _stack_instance
    if _stack_instance is None:
        _stack_instance=StackList()
    action=ns.action
    if action=="push":
        if ns.value is None:
            raise ValueError("stack push requires a value")
        _stack_instance.push(ns.value)
        return "ok"
    if action=="pop":
        return _stack_instance.pop()
    if action=="top":
        return _stack_instance.peek()
    if action=="len":
        return len(_stack_instance)
    raise ValueError("unknown stack action")
def _handle_queue(ns):
    global _queue_instance
    if _queue_instance is None:
        _queue_instance=QueueList()
    action=ns.action
    if action=="enqueue":
        if ns.value is None:
            raise ValueError("queue enqueue requires a value")
        _queue_instance.enqueue(ns.value)
        return "ok"
    if action=="dequeue":
        return _queue_instance.dequeue()
    if action=="front":
        return _queue_instance.front()
    if action=="len":
        return len(_queue_instance)
    raise ValueError("unknown queue action")
def build_parsers():
    parser=argparse.ArgumentParser(prog="lab3", add_help=True)
    subparsers=parser.add_subparsers(dest="command")


    p_fact=subparsers.add_parser("fact", help="factorial iterative")
    p_fact.add_argument("n", type=int)
    p_fact.set_defaults(func=_handle_fact)

    p_factr=subparsers.add_parser("factr", help="factorial recursive")
    p_factr.add_argument("n", type=int)
    p_factr.set_defaults(func=_handle_factr)


    p_fib=subparsers.add_parser("fib", help="fibonacci iterative")
    p_fib.add_argument("n", type=int)
    p_fib.set_defaults(func=_handle_fib)

    p_fibr=subparsers.add_parser("fibr", help="fibonacci recursive")
    p_fibr.add_argument("n", type=int)
    p_fibr.set_defaults(func=_handle_fibr)


    p_sort=subparsers.add_parser("sort", help="sort numbers")
    p_sort.add_argument("algo", choices=["bubble", "quick", "count", "radix", "bucket", "heap"])
    p_sort.add_argument("nums", nargs="+", type=float, help="numbers separated by spaces")
    p_sort.set_defaults(func=_handle_sort)


    p_stack=subparsers.add_parser("stack", help="stack operations")
    p_stack.add_argument("action", choices=["push", "pop", "top", "len"])
    p_stack.add_argument("value", nargs="?", type=int)
    p_stack.set_defaults(func=_handle_stack)


    p_queue=subparsers.add_parser("queue", help="queue operations")
    p_queue.add_argument("action", choices=["enqueue", "dequeue", "front", "len"])
    p_queue.add_argument("value", nargs="?", type=int)
    p_queue.set_defaults(func=_handle_queue)

    return parser
