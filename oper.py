#!/usr/bin/env python3
import sys

def parse_scores(args):
    """
    Parse a list of command-line arguments into a list of floats.
    """
    if not args:
        print("Usage: python scores.py <score1> <score2> ... <scoreN>")
        sys.exit(1)

    scores = []
    for a in args:
        try:
            scores.append(float(a))
        except ValueError:
            print(f"Invalid score: {a!r}. All scores must be numeric.")
            sys.exit(1)
    return scores

def main():
    # sys.argv[0] is the script name, scores start from sys.argv[1:]
    scores = parse_scores(sys.argv[1:])

    total = sum(scores)
    average = total / len(scores)

    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)

if __name__ == "__main__":
    main()
