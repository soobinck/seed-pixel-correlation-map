import numpy as np
import cv2
from tifffile import TiffFile


def to_npy(filename, **kwargs):
    if filename.endswith('.raw'):
        filename = raw2npy(filename, **kwargs)
    elif filename.endswith('.tif'):
        filename = tif2npy(filename)
    else:
        raise ImportError
    return filename


def raw2npy(filename_from, side_length):
    fp = np.fromfile(filename_from, dtype=np.single).byteswap()
    frame_dim = side_length * side_length
    if len(fp) % frame_dim:
        raise AssertionError
    num_frames = int(len(fp) / frame_dim)
    fp = fp.reshape(num_frames, side_length, side_length)
    # print(fp)
    # for i in range(num_frames):
    #     fp_1 = fp[i]
    #     cv2.imshow('', fp_1)
    return fp


def tif2npy(filename_from):
    with TiffFile(filename_from) as tif:
        tif_ary = tif.asarray()
        return tif_ary
