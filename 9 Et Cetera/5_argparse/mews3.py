
# use command line arguments instead of input

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()
#figures out arguments

for _ in range(int(args.n)):
    print("meow")