## LARKY

Github repo for SCDF X IBM Lifesavers’ Innovation Challenge: Call for Code 2020

### Team Members: 
Leona, Alvin, Ronnie, Kexin, Yongjia

## **Contents**
1. Short Description
2. Pitch Video
3. Architecture of solution
4. Hyperlink to detailed solution
5. Getting started
6. What we used to build the solution

## 1. **Short Description**

#### **Problem**

Seemingly harmless household objects may not seem to be an issue. However a pile up of such objects along corridors or the staircase can actually be a fire hazard and potential cause of fire. More commonly, unattended open flames in the kitchen is also a big fire hazard. It is therefore imperative to identify such fire hazards and prevent a fire from even breaking out.

However, significant manpower is needed to do regular checks and we feel that technology can be employed to reduce the manhours spent by fire safety managers and building operations managers on doing such checks in addition to their already taxing jobscopes. Also, it only takes a moment for disaster to strike and fires may break out at any time in between the regular checks. Hence, a constant monitoring system that can check and warn of fire hazards in critical areas will be of a big benefit to preventing disasters.
#
#### How technology can help

Our vision is to integrate our solution into the facilities that the Smart Nation initiative will be bringing, such as smarter CCTV cameras, Internet of Things and Cloud technology.

By programming a device to detect fire hazards through machine learning, an alert will be sent to the relevant stakeholders to inform them of the potential fire hazard in the area. They will be reminded to address this fire hazard, hence there is reduced likelihood of a fire breaking out.
#
#### Team Proposal

Our group proposes to leverage a network of smart infrastructure consisting of an automated fire hazard detection system to spot potential fire hazards.
#

## 2. **Pitch Video**

## 3. **Architecture of solution** 

![alt text][logo]

[logo]: https://github.com/alvinhuhhh/LARKY_SCDFXIBM/blob/master/framework.jpg

1. Every 1 minute, the camera takes a photo of the site.
2. The image is processed using the machine learning model made with IBM Watson Machine Learning Platform.
3. The machine learning model will help to determine if the image data contains any fire hazard.
4. The data is uploaded to Firebase Cloud Storage.
5. Web app is then used to retrieve this data from the cloud.
6. User can view this data on the app and be notified of the presence of fire hazard.

#
## 4. **Hyperlink to detailed solution**

[More details here](https://github.com/alvinhuhhh/LARKY_FireWatch_SCDFXIBM/blob/master/detailed_solution.txt)

#
## 5. **Getting started** 

#### Prerequisites:

pip, python and pyrebase must be installed before the start of the demo.

#### Installing:

Git clone the repo and change directory into it. pip install the package in 'requirement.txt' 

```
cd <directory to clone>
git clone https://github.com/alvinhuhhh/LARKY_FireWatch_SCDFXIBM.git
cd LARKY_FireWatch_SCDFXIBM
pip install -r requirement.txt
``` 

#### Running the Demo

First, open three terminals. Terminal 1 will run a "python-tflite.py", Terminal 2 will run "cloud.py" and Terminal 3 will act as the UI machine and run
"retrieve.py"
#
#### Detector Script
In terminal one, navigate to "detector_src/tflite_interpreter/basic" and run "python-tflite.py"

``` 
cd detector_src/tflite_interpreter/basic
python python-tflite.py
```

In our full scope, a camera will take a photo of the location and upload to the "detector_src_tflite_interpreter/basic/model/images" directory and store
the image as "location_ID.jpg", where ID is a number to identify the location. For demo purposes and hardware limitation, we provided an example photo
"location_1.jpg".

After running the python script, it will compare the photo against our model trained to identify fires in photos. The script will then output a "location_1.png" 
and "status_1.txt" to the "detector_src/tflite_interpreter/basic/model/output" directory.

The "status_1.txt" will contain a "1" if a fire is detected in the photo, or a "0" if the fire is not detected. The "location_1.png" file will contain the 
original photo with the detection frame to show whether there is a fire. 
#
#### Upload Script

In terminal two, navigate to "detector_src/tflite_interpreter/basic/model/output" and run "cloud.py"

```
cd detector_src/tflite_interpreter/basic/model/output
python cloud.py
```

This python script will make use of pyrebase and upload the "location_1.png" and "status_1.txt" file into Firebase storage, to be retrieved by the UI-side.
#
#### Retrieve Script and HTML UI

Assuming terminal three is in our UI machine. Navigate to "ui_src" and run "retrieve.py"

```
cd ui_srcpython 
python retrieve.py 
```

This script will retrieve the files from Firebase. In our full scope, there will be many location and status file, but for the demo, we assume there is
only one location and status. The script will first download the status.txt and check if it contains a "1" or "0". If it contains a "1", it shows that
there is fire detected in the photo and the script will then download the photo as well.

Next, open the "index.html" file in a browser. This will show a list of location. A green tick will indicate that there is no fire detected at the location, while a photo will indicate that there is fire detected in the location.

This concludes a full flow demo of our web alert system. To test it with other photos, you can add any photo in the 
"detector_src/tflite_interpreter/basic/model/images" directory and rename it location_1.jpg to try. Take note that the script runs indefinitely so you do not have to restart the script, as it will auto update in a timed-interval. After about 1 minute, refresh the HTML UI to see the changes. 

#
## 6. **What our team used to build our solution** 
* IBM Watson Machine Learning instance.

* IBM Cloud Annotations for localisation and detection.

* IBM Cloud Object Storage for storing data used to train our machine learning model.

* Firebase Cloud storage for image data to be uploaded and downloaded
#
