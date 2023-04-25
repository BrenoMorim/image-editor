import sys
import argparse
from validator import Validator, VALID_TYPES, VALID_ACTIONS
from editor import execute


def main():
    try:
        # The argparse library can throw exceptions, which we need to catch
        parser = argparse.ArgumentParser(description="CLI for image edition")
        parser.add_argument("-i", "--input", help=f"File to be used as source {VALID_TYPES}", required=True)
        parser.add_argument("-o", "--output", help=f"File to store the result {VALID_TYPES}", required=True)
        parser.add_argument("-a", "--action", help="Action to be applied in the image", required=True, choices=VALID_ACTIONS)
        parser.add_argument("-s", "--size", help="Specify the new size of the image, if the action chosen is resize. Format: WidthxHeight, like 1920x1080", required=False)
        args = parser.parse_args()
        # During the validation, exceptions can be raised as well
        valid_args = Validator(args.input, args.output, args.action, args.size)
        try:
            # Executes the required action 
            execute(valid_args)
            print(f"Operation completed successfully! Result saved in file {args.output}")
        except Exception:
            # A Pillow exception can occur, which we need to catch and show a proper message to the user
            sys.exit(f"It was not possible to apply the action {args.action} to the image {args.input}")
    except Exception as ex:
        sys.exit(ex)


if __name__ == "__main__":
    main()
