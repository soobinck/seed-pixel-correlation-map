import os
from open_file import to_npy
import matplotlib.cm as cm
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from iterate_thr_files import mask_filtered_files
import argparse
from get_seeds import get_seeds

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', required=True)
parser.add_argument('-s', '--seeds', required=True)
io_args = parser.parse_args()
path = io_args.path
path_to_seeds = io_args.seeds

os.makedirs(os.path.join(path, 'seed_maps'), exist_ok=False)

resolution = 128

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
        seed_loc = np.zeros((frames, 1, 1))
        seed_loc = im[:, seeds[seed]['X'], seeds[seed]['Y']]

        pears = np.zeros((resolution, resolution))
        for i in range(resolution):
            for j in range(resolution):
                if mask[i][j] == 0:
                    pears[i][j] = None
                else:
                    pears[i][j] = pearsonr(seed_loc,
                                           im[:, i, j])[0]

        ax = sns.heatmap(pears, cmap=cm.jet, vmin=0, vmax=1, square=True)
        ax.set_facecolor('xkcd:black')
        fig = ax.get_figure()
        plt.title('seed pixel correlation')
        fig.savefig(os.path.join(path, 'seed_maps' , filtered_file['file'][:3] + seed))
        plt.clf()
