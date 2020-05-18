import argparse
import os

import matplotlib.cm as cm
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

from get_seeds import get_seeds
from iterate_thr_files import mask_filtered_files
from open_file import to_npy
from pearsonr_matrix import pearsonr_matrix

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', required=True)
parser.add_argument('-s', '--seeds', required=True)
parser.add_argument('-r', '--resolution', default=128)
io_args = parser.parse_args()
path = io_args.path
path_to_seeds = io_args.seeds
resolution = io_args.resolution

os.makedirs(os.path.join(path, 'seed_maps'), exist_ok=False)

mask, filtered_files = mask_filtered_files(path)

seeds = get_seeds(path_to_seeds)

mask = to_npy(mask)

for seed in seeds:
    for filtered_file in filtered_files:
        if filtered_file['file'].endswith('tif'):
            im = to_npy(os.path.join(filtered_file['root'], filtered_file['file']))
        else:
            im = to_npy(os.path.join(filtered_file['root'], filtered_file['file']), side_length=resolution)

        frames = im.shape[0]

        seed_loc = im[:, seeds[seed]['Y'], seeds[seed]['X']]
        seed_loc = np.dstack([seed_loc] * (resolution * resolution))
        seed_loc = seed_loc.reshape(frames, resolution, resolution)
        pears = pearsonr_matrix(seed_loc, im)
        mask_idx = np.where(mask == 0)
        pears[mask_idx] = None

        ax = sns.heatmap(pears, cmap=cm.jet, vmin=0, vmax=1, square=True)
        ax.set_facecolor('xkcd:black')
        # ax.invert_yaxis()
        fig = ax.get_figure()
        plt.title('seed pixel correlation')
        fig.savefig(os.path.join(path, 'seed_maps', filtered_file['file'][:3] + seed))
        plt.clf()
