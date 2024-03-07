from moviepy.editor import *
import os
import csv
import logging
from tqdm import tqdm
import shutil
import argparse

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

#convert mm:ss to total seconds
def get_seconds(time_str):
    # split in mm, ss
    mm, ss = time_str.split(':')
    return int(mm) * 60 + int(ss)

#close the video before exiting the program
def quit():
    video.close()
    exit()

#read the csv file
def get_timestamps():
    timestamps = []
    timestamps_duplicates = []
    try:
        with open(f'./{args.timestamps}', 'r') as file:
            csvreader = csv.reader(file)
            #skip headers
            next(csvreader, None)
            for row in csvreader:
                #get any duplicates
                if row in timestamps:
                    timestamps_duplicates.append(row)

                timestamps.append(row)

        #terminate if any csv duplicates
        if len(timestamps_duplicates) > 0:
            raise ValueError
                
    except FileNotFoundError:
        logging.error('CSV File Not Found, please check file name or file location')
        quit()
    except ValueError:
        logging.error('The following csv values are duplicates, please ensure unique values.')
        logging.info(timestamps_duplicates)
        quit()
    except:
        logging.error('Could not read the CSV file')
        quit()
    return timestamps


def get_Video():
    try: 
        #scale video if arg is provided
        video = VideoFileClip(f'./{args.video}').resize(args.output_scale) if args.output_scale else VideoFileClip(f'./{args.video}')
        return video
        
    except OSError:
        logging.error('Video File Not Found, please check file name or file location')
        exit()
    except:
        logging.error('Could not load specified video')
        exit()

#new dir for all gifs
def createDir(video_name):
    dir = f'./{video_name}_gifs'
    #delete any existing dir
    try:
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)
        return dir
    except:
        logging.error('Could not create a GIFs directory')
        quit()


def createGifs(video):
    #remove the .mp4 for naming files
    video_name = args.video.split('.')[0]
    timestamps = get_timestamps()
    gifs_dir = createDir(video_name)

    logging.info(f'Generating a total of {len(timestamps)} Gifs...')

    #tqdm is the progress bar
    for timestamp in tqdm(timestamps, ncols=120, unit='gif'):
        trim_from = get_seconds(timestamp[0])
        trim_to = trim_from + int(timestamp[1])
        timestamp_for_name = timestamp[0].replace(':','')

        video.subclip(trim_from, trim_to).write_gif(f'{gifs_dir}/{video_name}_{timestamp_for_name}.gif', program='ffmpeg', logger=None)
    
    logging.info('Done!')


#args
parser = argparse.ArgumentParser()
parser.add_argument('video', help='Video to generate GIFs from')
parser.add_argument('timestamps', help='CSV file with timestamps and respective GIF duration')
parser.add_argument('--output_scale', type=float, help='Scale of generated GIFs')
args = parser.parse_args()

video = get_Video()
createGifs(video)


# [done] properly use logging
# [done] check for timestamp duplicates
# [done] resizing: edited Lib\site-packages\moviepy\video\fx\resize.py, line 37: Image.Antialias (deprecated) -> Image.Resampling.LANCZOS 

