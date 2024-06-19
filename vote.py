#!/usr/bin/env python

from random import shuffle

def main():
    with open("decisions.txt") as f:
        decisions = f.readlines()

    shuffle(decisions)
    decision = decisions.pop().strip()
    print(decision)

if __name__ == '__main__':
    main()
