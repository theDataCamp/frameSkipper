#must have openCV, can use command pip install opencv-python
import cv2
import argparse
import os
from os import path

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="string of file path", required=True)
parser.add_argument("-o", "--out-dir", help="output directory location", required=True)
parser.add_argument("-n", "--skip-n-frames", help="determine how many frames to skip", type=int, required=True)

def FrameCapture(path, skip_n_frames, outfile):

    vidObj = cv2.VideoCapture(path)
    count = 0
    pic_count = 1
    success = 1
    total_frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"total frame {total_frames}")
    while success:
        success, image = vidObj.read()
        if count % skip_n_frames == 0:
            cv2.imwrite(f"{outfile}frame_{pic_count}.jpg", image)
            pic_count +=1
        count +=1
    print(f"Created {pic_count} images")

if __name__ == '__main__':
    args = parser.parse_args()
    
    if path.exists(args.file):
        if path.isdir(args.out_dir):
            FrameCapture(args.file, skip_n_frames = args.skip_n_frames, outfile = args.out_dir)
        else:
            print("Directory does not exists")
            quit()
    else:
        print("File does not exist")
        quit()



