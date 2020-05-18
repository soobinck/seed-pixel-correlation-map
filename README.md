# seed-pixel-correlation-map(SPCM)

Input:

(1) a directory containing .tif or .raw files to analyze and Mask.tif. 
 
(2) seeds location. 

(3) optional: resolution in pixels

Output:

a directory named `seed_maps` containing SPCMs.

Syntax: 

`python main.py -p/--path <path> -s/--seeds <seeds> -r/--resolution <resolution>`

<br/><br/>

## Welcome to my seed-pixel-correlation-map repository! 

This is a simple piece of code that generates SPCMs(or just correlation maps) given the location of seeds. 

The following instruction to run the script assumes the following file structure:

```
|
|-- seed-pixel-correlation-map (your current directory, use pwd to check!)
|
|-- data
  |
  |-Mask.tif
  |-Images_to_analyze.tif
  |-Images_to_analyze.raw
  |-seeds.py

```


To run this code, please follow these steps:

1. Download the zip file and unzip.

2. Find where your `Mask.tif` file and `Images_to_analyze.raw/.tif` are. Put them under the same directory.

3. Using your terminal, `cd`(change directory) to `seed-pixel-correlation-map`.

4. On your terminal, type `python main.py -p ../data -s ../data/seeds.py` if your Images has the dimension of 128 pixels by 128 pixels. If not, (if it's 512 for example) type `python main.py -p ../data -s ../data/seeds.py -r 512`

5. Hit return/enter like you mean it!

6. Check your `data` folder and look for `seeds_maps` folder!

<br/><br/>

Notes:

- The directory `<path>` **must** contain `Mask.tif`, _or it will return an error_.

- For the format of seed file, please see `seeds_example.py`.

- `data` should not have a directory named `seed_maps`, _or it will return an error_. 
  
<br/><br/>

Tested on MacOS Catalina. I do not have a Windows machine so I couldn't test it on that OS. To guarantee the script to run, put all of the data (Mask.tif, seeds.py and Images_to_analyze.raw/.tif) into `seed-pixel-correlation-map` and run `python main.py -p ./ -s ./seeds.py` (or if your pics have a resolution other than 128, let's say 512, run `python main.py -p ./ -s ./seeds.py -r 512`).
