import numpy as np


def pearsonr_matrix(seed, im):
    cov = np.sum((im - im.mean(axis=0)) * (seed - seed.mean(axis=0)), axis=0)
    sd_im = np.sqrt(np.sum((im - im.mean(axis=0)) ** 2, axis=0))
    sd_seed = np.sqrt(np.sum((seed - seed.mean(axis=0)) ** 2, axis=0))
    return cov/(sd_im*sd_seed)

