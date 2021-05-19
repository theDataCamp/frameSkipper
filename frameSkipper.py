import cv2

vidPath = "vid/path/here"


def FrameCapture(path, skip_n_frames):

    vidObj = cv2.VideoCapture(path)
    count = 0
    pic_count = 1

    success = 1

    while success:
        success, image = vidObj.read()
        if count % skip_n_frames == 0:
            cv2.imwrite(f"frame_{pic_count}.jpg", image)
            pic_count +=1
        count +=1

if __name__ == '__main__':
    FrameCapture(vidPath, skip_n_frames=120)

