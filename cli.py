"""Command-line interface for the 24-game solver."""

import argparse

from solver import solve_24


def main():
    """Parse command-line arguments and executes the 24-game solver."""
    parser = argparse.ArgumentParser(description="A modular 24-Game Solver.")

    parser.add_argument(
        "cards",
        metavar="N",
        type=int,
        nargs="+",
        help="The integer cards to solve for (e.g., 4 7 8 8)",
    )

    args = parser.parse_args()

    print(f"Running solver for cards: {args.cards} ...\n")

    results = solve_24(args.cards)

    if results:
        print(f"Found {len(results)} solution(s):")
        for res in results:
            print(f"  {res} = 24")
    else:
        print("No solutions found for these cards.")


if __name__ == "__main__":
    main()
