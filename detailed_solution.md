## Software Framework
1. We used IBM Cloud Annotations to train a model to identify lit kitchen hobs in kitchens. Required service connections to other IBM Services such as IBM Watson Machine Learning instance and IBM Cloud Object Storage.
2. After downloading the model from IBM Cloud Annotations, the model is used in a Python script(python-tflite.py) to classify images taken by a camera. The photo will be taken by external cameras every 1 minute at many location and it will be uploaded to a specific directory for the python script to compare against the model, as "location_ID.jpg", where ID is an integer to identify the location.
3. After comparing against the model, the script will save the photo annotated with detection frame in a location_ID.png image file as well as a status_ID.txt file to indicate whether fire is detected.
4. Next, another Python script(cloud.py) handles the upload of the images and data to Firebase Cloud Storage.
5. Our frontend will be a Web UI based on Python Django, although it is not implemented yet. We will use a simple .HTML to represent our Web UI.
6. A Python script from the UI machine(retrieve.py) will handle the downloading of data from Firebase Cloud Storage, which will then be displayed via the Web UI if the status shows that there is fire. Else, the Web UI will show a green tick corresponding to the location.
7. We intend to utilise the network of CCTV and other small cameras placed in strategic/critical locations to monitor areas, and the Web UI will provide real-time updates on each camera.

## Hardware Architecture
1. All CCTVs and other cameras will be connected to a indepedent machine using a small plugin device (such as Raspberry Pi). Each device will control it's own camera and upload the files independently to Firebase.
2. A seperate machine will then act as the central server and connect to the Internet to access Firebase.
3. The machine acting as central server will serve the .HTML UI as well as retrieving files from Firebase to server. 

## Explanation of Files
Relative Directory: /detector_src/tflite_interpreter/basic

1. python-tflite.py script will handle the photo input and setting it up for comparison against the model supplied.

2. /model/model_data stores the relative model files that we have from training the model to identify fires.
3. /model/images will store all image files taken from the camera
4. /model/output will store the image file as well as the status file after the comparison has been made.
5. /model/output/cloud.py script will handle the photo and status uploading to Firebase

6. /utils/cacli_models.py script will handle the actual comparison logic between the model and the image supplied 
7. /utils/label_map_util.py and visualization_utils.py are miscellaneous utils files.

Relative Directory: /ui_src

1. index.html is our simple web-based UI that is designed for google chrome
2. retrieve.py script will handle the files downloading from Firebase
3. ok_icon.png contains the photo for the default Green Tick, to show that there is no fire detected.

## Main flow of events

1. Camera take a photo of a location every 1 minute
2. Photo compared against a model and results are uploaded to Firebase in a 1 minute interval

1. UI Machine will download photos from Firebase every 10 seconds to ensure the UI is updated frequently.
2. Photos will be shown on HTML if there is a fire detected, else a green tick will be shown. 
