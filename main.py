import argparse
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageChops


def remove_white(img) -> Image:
    background = Image.new('RGB', img.size, img.getpixel((0,0)))
    diff_img = ImageChops.difference(img, background)
    crop_range = diff_img.convert('RGB').getbbox()
    crop_img = img.crop(crop_range)
    
    return crop_img


def split_image(img) -> tuple:
    width, height = img.size
    box = (0, 0, int(width / 2) - 1, height)
    left_img = img.crop(box)
    box = (int(width / 2), 0, width - 2, height)
    right_img = img.crop(box)
    
    if left_img.size != right_img.size:
        print(left_img.size, right_img.size)
        right_img = right_img.resize(left_img.size, Image.LANCZOS)
    
    left_img.save('left.png')
    right_img.save('right.png')
    return np.array(left_img), np.array(right_img)


def main():
    
    parser = argparse.ArgumentParser(description='Find the difference between two similar images aligned on the left and right.')
    parser.add_argument('--input', '-i', type=str, default='body.png', help='input image path')
    parser.add_argument('--output', '-o', type=str, default='diff', help='output image path')
    args = parser.parse_args()
    
    input_path = Path(args.input)
    
    img = Image.open(input_path)
    img = remove_white(img)
    left, right = split_image(img)
    
    diff = left.astype(int) - right.astype(int)
    diff = np.abs(diff)
    cv2.imwrite('diff.png', diff)
    

if __name__ == "__main__":
    main()