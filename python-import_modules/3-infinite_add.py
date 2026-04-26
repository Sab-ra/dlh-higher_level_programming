#!/usr/bin/python3
import sys

if __name__ == "__main__":
    for i in sys.argv[1:]:
        print(sum(int(i)))
