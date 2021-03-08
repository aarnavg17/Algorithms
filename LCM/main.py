import sys

sys.path.insert(0, '/Users/aarnavg17/Desktop/Github/Algorithms/GCD')

import GCD


def lcm(a, b):
    return (a * b) / GCD.GCD(a, b)
