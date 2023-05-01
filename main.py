import argparse
from pathlib import Path

from PIL import Image

parser = argparse.ArgumentParser(description='Find the difference between two similar images aligned on the left and right.')
parser.add_argument('--input', '-i', type=str, required=True, help='input image path')
parser.add_argument('--output', '-o', type=str, default='diff', help='output image path')
args = parser.parse_args()

def main():
    img = Image.open(args.input)
    

if __name__ == "__main__":
    main()