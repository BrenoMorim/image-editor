import sys
import argparse
from validator import Validator, VALID_TYPES, VALID_ACTIONS
from editor import execute


def main():
    try:
        # The argparse library can throw exceptions, which we need to catch
        parser = get_parser()
        # During the validation, exceptions can be raised as well
        valid_args = validate_arguments(parser)
        # Executes the action
        handle_execution(valid_args)
    except Exception as ex:
        sys.exit(ex)


def get_parser() -> argparse.ArgumentParser:
    """
    Prepares the argparse.ArgumentParser object that will encapsulate the command line arguments
    """
    parser = argparse.ArgumentParser(description="CLI for image edition")
    parser.add_argument("-i", "--input", help=f"File to be used as source {VALID_TYPES}", required=True)
    parser.add_argument("-o", "--output", help=f"File to store the result {VALID_TYPES}", required=True)
    parser.add_argument("-a", "--action", help="Action to be applied in the image", required=True, choices=VALID_ACTIONS)
    parser.add_argument("-s", "--size", help="Specify the new size of the image, if the action chosen is resize. Format: WidthxHeight, like 1920x1080", required=False)
    return parser


def validate_arguments(parser: argparse.ArgumentParser) -> Validator:
    """
    Given an ArgumentParser, returns a Validator object containing only valid data extracted
    from the CLI. If an invalid arguments is passed, an Exception will be raised
    """
    args = parser.parse_args()
    return Validator(args.input, args.output, args.action, args.size)


def handle_execution(valid_args: Validator) -> None:
    """
    Handles the execution of the specified action, making sure to
    catch errors if one is raised during the process
    """
    try:
        # Executes the required action 
        execute(valid_args)
        print(f"Operation completed successfully! Result saved in file {valid_args.output}")
    except Exception:
        # A Pillow exception can occur, which we need to catch and show a proper message to the user
        sys.exit(f"It was not possible to apply the action {valid_args.action} to the image {valid_args.input}")


if __name__ == "__main__":
    main()
