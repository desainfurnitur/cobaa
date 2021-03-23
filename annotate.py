import os
import sys
import tkinter as tk
from tkinter import filedialog

import config as c
from Positive_feedback.load_from_image import PF_from_IPTC
from Positive_feedback.object_detection import run_detector
from Positive_feedback.image_classification import clasify

"""Opens a dialog to choose input, user can choose multiple images"""


def pop_up():
    root = tk.Tk()
    root.withdraw()
    return list(filedialog.askopenfilenames(title="Choose files to annotate", initialdir=c.INITIALDIR))


def build_PF(path_to_image):
    from_image_IPTC = PF_from_IPTC(path_to_image)
    #from_object_detection = run_detector(c.OD_PATH, path_to_image)
    images = [path_to_image]
    for filename in os.listdir(c.TEMP_PATH):
        if filename.startswith("boxes"):
            images.append(c.TEMP_PATH + filename)
    from_image_classification = clasify(images)
    print()


if __name__ == '__main__':
    if c.POPUP or len(sys.argv) == 1:
        input_path = pop_up()
    else:
        input_path = sys.argv[1:]
    build_PF(input_path[0])