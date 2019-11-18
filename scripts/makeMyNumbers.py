
from numpy.random import shuffle
import argparse

parser = argparse.ArgumentParser(description='Add a sample numbe')
parser.add_argument('sample', type=int,
                    help='How many repetitions of each digit')

args = parser.parse_args()

def make_numbers(samples):
    out = [n for _ in range(samples) for n in range(10)]
    shuffle(out)
    return out

if __name__ == '__main__':
    print(make_numbers(args.sample))
