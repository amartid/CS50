
# use command line arguments instead of input

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()
#figures out arguments

for _ in range(int(args.n)):
    print("meow")