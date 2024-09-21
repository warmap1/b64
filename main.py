import base64
import argparse
import sys

parser = argparse.ArgumentParser(description="Utils for base64")
parser.add_argument(
    "-e",
    type=str,
    nargs="?",
    const=True,
    metavar="<TEXT>",
    help="Encrypts text",
)
parser.add_argument(
    "-d",
    type=str,
    nargs="?",
    const=True,
    metavar="<TEXT IN B64>",
    help="Decrypts text",
)
parser.add_argument(
    "-q",
    type=bool,
    metavar="<True/False>",
    help="Give only encoded/decoded text (quiet mode)",
)
parser.add_argument(
    "--debug",
    type=bool,
    metavar="<True/False>",
    help="Debug mode",
)

args = parser.parse_args()
t2e = args.e
t2d = args.d
q = args.q
debugger = args.debug

def debug():
    if debugger:
        print("Arguments:", args)
        print("Text to Encrypt:", t2e)
        print("Text to Decrypt:", t2d)

if __name__ == "__main__":

    # Check t2d or t2e from | or >/<
    if t2d is True:
        if not sys.stdin.isatty():
            input_data = sys.stdin.read().strip()
            t2d = input_data
        else:
            parser.print_help()
            sys.exit(1)
    if t2e is True:
        if not sys.stdin.isatty():
            input_data = sys.stdin.read().strip()
            t2e = input_data
        else:
            parser.print_help()
            sys.exit(1)

    # Encrypt/Decrypt
    if t2e:
        debug()
        result = base64.b64encode(t2e.encode()).decode("utf-8")
        if not q:
            print("Result:", result)
        else:
            print(result)

    if t2d:
        debug()
        try:
            result = base64.b64decode(t2d.encode()).decode("utf-8")
            if not q:
                print("Result:", result)
            else:
                print(result)
        except Exception as e:
            print(f"Error: {e}")

    if not t2e and not t2d:
        parser.print_help()
        sys.exit(1)
