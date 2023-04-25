import sys
import argparse
from validator import Validator, VALID_TYPES, VALID_ACTIONS
from editor import execute


def main():
    try:
        parser = argparse.ArgumentParser(description="CLI for image edition")
        parser.add_argument("-i", "--input", help=f"File to be used as source {VALID_TYPES}", required=True)
        parser.add_argument("-o", "--output", help=f"File to store the result {VALID_TYPES}", required=True)
        parser.add_argument("-a", "--action", help=f"Action to be applied in the image", required=True, choices=VALID_ACTIONS)
        args = parser.parse_args()
        valid_args = Validator(args.input, args.output, args.action)
        try:
            execute(valid_args)
            print(f"Operation completed successfully! Result saved in file {args.output}")
        except Exception:
            sys.exit(f"It was not possible to apply the action {args.action} to the image {args.input}")
    except Exception as ex:
        sys.exit(ex)

if __name__ == "__main__":
    main()
