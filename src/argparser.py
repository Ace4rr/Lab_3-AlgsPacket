import argparse
from algos.factorial import factorial

def build_parsers():
    parser=argparse.ArgumentParser(prog="",add_help=False)
    subparsers=parser.add_subparsers(dest=("command"))

    p_fact=subparsers.add_parser("fact", help="factorial")
    p_fact.add_argument("n", type=int)
    p_fact.set_defaults(handler=factorial, mode="iter")

    p_factr=subparsers.add_parser("factr", help="factorial recursive")
    p_factr.add_argument("n", type=int)
    p_factr.set_defaults(handler=factorial, mode="rec")


    p_fib=subparsers.add_parser("fib", help="fibonacci iterative")
    p_fib.add_argument("n", type=int)
    p_fib.set_defaults(handler=factorial, mode="iter")

    p_fibr=subparsers.add_parser("fibr", help="fibonacci recursive")
    p_fibr.add_argument("n", type=int)
    p_fibr.set_defaults(handler=factorial, mode="rec")


    p_sort=subparsers.add_parser("sort", help="run a sorting algorithm")
    p_sort.add_argument("algo", choices=["bubble", "quick", "count", "radix", "bucket", "heap"])
    p_sort.add_argument("nums", nargs="+", type=float)
    p_sort.set_defaults(handler=factorial)

    p_stack=subparsers.add_parser("stack", help="stack operations")
    p_stack.add_argument("action", choices=["push", "pop", "top"])
    p_stack.add_argument("value", nargs="?", type=int)
    p_stack.set_defaults(handler=factorial)

    return parser
