# seed-pixel-correlation-map

To run this script, run: `python main.py -p <path> -s <seed>` or `python main.py -p <path> -s <seed> -r <resolution>`. The default resolution 128 pixels per side length.

The directory `<path>` **must** contain `Mask.tif`, _or it will return an error_.

`<seed>` is the path to a python file including the x, y coordinates of the seeds (for example, `data/seeds.py`). For the format of seed file, please see `seeds_example.py`.

Seed pixel correlation map .png files will be genereated to `<path>` under the directory `seed_maps`. <path> should not have a directory named `seed_maps`, _or it will return an error_. 


Tested on MacOS Catalina.
