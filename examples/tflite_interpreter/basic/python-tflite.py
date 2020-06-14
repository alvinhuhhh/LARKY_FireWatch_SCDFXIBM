#!/usr/bin/python
# Matthew Dunlop, August 2018
# https://github.com/mdunlop2
#
# Contact:
# https://www.linkedin.com/in/mdunlop2/

#Code taken from https://github.com/cloud-annotations/object-detection-python
#Modified by LARKY team

import glob
import os
import time

import argparse

from utils import visualization_utils as vis_util
from utils import cacli_models as models


# Directory in which this example takes place
CURRENT_DIR = os.getcwd()

# Optional User Inputs
parser = argparse.ArgumentParser(description='Perform cacli tflite model inference')
parser.add_argument('--MODEL_DIR', default = CURRENT_DIR + "/model/model_data",
                   help='Give the path to your folder containing model.tflite, anchors.json and labels.json')

parser.add_argument('--MINIMUM_CONFIDENCE', default = 0.6,
                   help='Minimum score for an object to be considered for plotting')

parser.add_argument('--PATH_TO_TEST_IMAGES_DIR', default = CURRENT_DIR + "/model/images",
                   help='Path to folder containing images (.jpg) to test model on')

parser.add_argument('--PATH_TO_OUTPUT_DIR', default = CURRENT_DIR + "/model/output",
                   help='Path to folder where model will place output images')

a = parser.parse_args()

TEST_IMAGE_PATHS = glob.glob(os.path.join(a.PATH_TO_TEST_IMAGES_DIR, '*.jpg'))
MODEL_PATH = a.MODEL_DIR + "/model.tflite"
MODEL_ANCHOR_PATH = a.MODEL_DIR + "/anchors.json"
MODEL_LABEL_PATH = a.MODEL_DIR + "/labels.json"

print(a.MODEL_DIR)
# Load model and allocate tensors
model_interpreter = models.initiate_tflite_model(MODEL_PATH)
# Load mobilenet-v1 anchor points
anchor_points = models.json_to_numpy(MODEL_ANCHOR_PATH)

# Load Category Index
label_list = models.json_to_numpy(MODEL_LABEL_PATH)

category_index = { i : {"name" : label_list[i]} for i in list(range(len(label_list))) }
count= 0

while True:
    
    
    print("Starting to detect..") #compare the photo taken and run the comparison with the model to detect fire every 60 seconds
    for image_path in TEST_IMAGE_PATHS:
        models.detect_objects(model_interpreter,
                        image_path,
                        category_index,
                        anchor_points,
                        a.MINIMUM_CONFIDENCE,
                        SAVE_DIR=a.PATH_TO_OUTPUT_DIR)
    print("Done detecting.. System will sleep for 60 seconds")
    time.sleep(60)
