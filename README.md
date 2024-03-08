# Shotlist Maker

## Brief
Generates GIFs from a video file based on a timestamps csv file.

## Setup
Files needed in the current directory: video file, timestamps csv file
Format of the csv file: [timestamp (##:##), gif_duration (seconds)] -> e.g. [1:12, 5]
Installing requirements:
''' python
pip install requirements.txt
'''
Fix needed in the moviepy package for the resizing function:
Lib\site-packages\moviepy\video\fx\resize.py, line 37: Image.Antialias (deprecated) -> Image.Resampling.LANCZOS

## Usage
CMD line format: py videoGifs.py <video_filename> <timestamps_filename.csv> <--optional output_scale>
If the scale argument is not given, GIFs will have the same size as the original video file
CMD line example: 
''' python
py videoGifs.py untouchable.mp4 timestamps.csv --output_scale 0.2
'''
