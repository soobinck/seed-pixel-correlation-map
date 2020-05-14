# seed-pixel-correlation-map

To run this script, run: `python main.py -p <path> -s <seed>`.

The directory `<path>` **must** contain `Mask.tif`, or it will return an error.

`<seed>` is the path to the python document including the x, y coordinates of the seeds (for example, `data/seeds.py`).

Seed pixel correlation map .png files will be genereated to `<path>` under the directory `seed_maps`.

