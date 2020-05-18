# seed-pixel-correlation-map(SPCM)

Input:

(1) a directory containing .tif or .raw files 

(2) Mask.tif 

(3) seeds location. 
<br />
<br />
Output: a directory named `seed_maps` containing SPCMs.

Welcome to my seed-pixel-correlation-map repository! 

This is a simple piece of code that generates SPCMs(or just correlation maps) given the location of seeds. 

To run this code, please follow these steps:

1. Download the zip file and unzip.

2. Using your terminal, `cd`(change directory) to the file where these files are stored.

3. 





To run this script, run: `python main.py -p <path> -s <seed>` or `python main.py -p <path> -s <seed> -r <resolution>`. The default resolution is 128 pixels per side length.

The directory `<path>` **must** contain `Mask.tif`, _or it will return an error_.

`<seed>` is the path to a python file including the x, y coordinates of the seeds (for example, `data/seeds.py`). For the format of seed file, please see `seeds_example.py`.

Seed pixel correlation map .png files will be genereated to `<path>` under the directory `seed_maps`. <path> should not have a directory named `seed_maps`, _or it will return an error_. 
  



Tested on MacOS Catalina.
