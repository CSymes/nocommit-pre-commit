#!/usr/bin/env python

import subprocess
import sys
import argparse

class Colours:
    RED = "\033[0;31m"
    BRED = "\033[1;31m"
    RESTORE = "\033[0m"

def main():
    parser = argparse.ArgumentParser(description='Pre-commit hook to check for a specific phrase in staged files.')
    parser.add_argument('--searchstr', default='nocommit', help='The phrase to search for (default: nocommit)')
    parser.add_argument('remaining_files', nargs='*', help='Remaining files to check')
    args = parser.parse_args()

    try:
        diff_files = subprocess.check_output(
            ['git', 'diff', '--staged', '-i', '--diff-filter=d', '--name-only', '-G', args.searchstr] + args.remaining_files,
            text=True).splitlines()
    except subprocess.CalledProcessError:
        sys.exit(1)

    if diff_files:
        print(f"{Colours.BRED}Error: commit gate phrase '{args.searchstr}' was found in {len(diff_files)} file(s):{Colours.RESTORE}")
        print(Colours.RED + '\n'.join(diff_files) + Colours.RESTORE)
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
