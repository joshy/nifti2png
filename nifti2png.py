import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional

import nibabel as nib
import numpy as np
from skimage import img_as_ubyte
from skimage.exposure import equalize_adapthist

from PIL import Image
from tqdm import tqdm

def process(input_dir, output_dir):
    files = list(input_dir.resolve().glob("**/*.nii"))
    for f in tqdm(files):
        nifti = nib.load(str(f))
        image = nifti.get_data()
        if image.ndim == 3:
            image = image[:, :, 0]
        if image.ndim == 4:
            image = image[:, :, 0, 0]
        image = np.flipud(np.rot90(image))
        image = equalize_adapthist(image)
        image = img_as_ubyte(image)
        filename = output_dir / (f.stem + ".png")
        temp_image = Image.fromarray(image)
        temp_image.save(filename)


def run():
    # call example
    # python nifti2png --dir /data/example-dir --out /data/output
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=Path, help="Starting directory")
    parser.add_argument("-o", "--out", type=Path, help="Output directory")
    args = parser.parse_args()

    if not (args.dir or args.out):
        print("--dir or --out parameter missing, exiting")
        exit(1)

    print("Running on dir", args.dir)

    if not args.out.is_dir():
        print(f"Output directory {args.out} is missing, creating it")
        args.out.mkdir(parents=True, exist_ok=True)

    process(args.dir, args.out)
    exit(0)


run()
