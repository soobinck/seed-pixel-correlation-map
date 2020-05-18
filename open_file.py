import numpy as np
import cv2
from tifffile import TiffFile


def to_npy(filename, **kwargs):
    if filename.endswith('.raw'):
        filename = raw2npy(filename, **kwargs)
    elif filename.endswith('.tif'):
        filename = tif2npy(filename)
    else:
        raise ImportError("No file to import.")
    return filename


def raw2npy(filename_from, side_length):
    fp = np.fromfile(filename_from, dtype=np.single).byteswap()
    frame_dim = side_length * side_length
    if len(fp) % frame_dim:
        raise AssertionError("The total number of pixels are not divisible by the given side length (default 128).")
    num_frames = int(len(fp) / frame_dim)
    fp = fp.reshape(num_frames, side_length, side_length)

    return fp


def tif2npy(filename_from):
    with TiffFile(filename_from) as tif:
        tif_ary = tif.asarray()
        return tif_ary
