# Shotlist Maker

## Brief
Generates GIFs from a video file based on a timestamps provided a csv file.

## Setup
- Installing requirements:

``` 
    pip install requirements.txt
```

- Fix needed in the moviepy package for the resizing function:
    - Lib\site-packages\moviepy\video\fx\resize.py, line 37: Image.Antialias (deprecated) -> Image.Resampling.LANCZOS

## Usage
Use the script in commandline with the following input arguments below:

```
py videoGifs.py <video_filepath> <timestamps_filepath> <--output_scale>
```

- <video_filepath> : The filepath to the mp4 video you want to use. 
- <timestamps_filepath> : The filepath to the csv file with the timestamps and duration of each cut. 
- <--output_scale> : A floating point number defining a scale factor to enlarge of shrink the video on output. Default value is 1.  

Commandline example: 
``` 
py videoGifs.py untouchable.mp4 timestamps.csv --output_scale 0.2
```
### Timestamps csv format and example 
|timestamp (mm:ss)|duration (s)|
|-----------------|------------|
|01:34| 5| 
|02:34| 6| 
|3:00| 3| 

## Error checks
- Current implementation does not permit duplicated timestamps in the csv provided. 

## Future development 
- We will ensure that the timestamps are within the duration of the actual video 
- Ensure that data provided in the timestamp csv is non-negative. 


