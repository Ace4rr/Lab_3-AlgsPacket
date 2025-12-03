import shlex
from argparser import build_parsers
from logger import logger
parser=build_parsers()

def main():
    while True:
        try:
            raw=input("lab3> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if  raw.lower() in ("exit","quit"):
            break
        if not raw:
            continue 
        try:
            argv=shlex.split(raw)
            args=parser.parse_args(argv)
        except SystemExit:
            logger.warning(f"Argparse error")
            continue 
        except Exception as e:
            logger.warning(f"Parse error: {e}")
            print(f"Parse error: {e}")
            continue
        if not hasattr(args,"handler"):
            print("Unknown command")
            continue
        try:
            result=args.handler(args.n)
            print(result)
        except Exception as e:
            print(f"Error: {e}")
            logger.warning(f"Command failed{e}")
if __name__=="__main__":
    main()