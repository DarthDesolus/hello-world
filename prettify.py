#!/usr/bin/env python3

"""Simple JSON prettifier.

Usage:
    python3 prettify.py < input.json > output.json
    python3 prettify.py input.json
"""

import json
import sys


def read_input():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            return f.read()
    return sys.stdin.read()


def main():
    try:
        data = json.loads(read_input())
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Invalid JSON: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()


