#!/usr/bin/env python3

import argparse
import random

from .quotes import QUOTES
from .shamans import SHAMANS


def create_bubble(text):
    width = len(text)

    print(" " + "_" * (width + 2))
    print(f"< {text} >")
    print(" " + "-" * (width + 2))


def main():
    parser = argparse.ArgumentParser(
        prog="codeshaman",
        description="A motivational CLI inspired by cowsay."
    )

    parser.add_argument(
        "message",
        nargs="*",
        help="Custom message to display"
    )

    parser.add_argument(
        "--character",
        choices=SHAMANS.keys(),
        default="wizard",
        help="Choose a shaman character"
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List available shaman characters"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="CodeShaman 0.1.0"
    )

    args = parser.parse_args()

    if args.list:
        print("Available shamans:")
        for shaman in SHAMANS:
            print(f" - {shaman}")
        return

    if args.message:
        quote = " ".join(args.message)
    else:
        quote = random.choice(QUOTES)

    create_bubble(quote)
    print(SHAMANS[args.character])


if __name__ == "__main__":
    main()
