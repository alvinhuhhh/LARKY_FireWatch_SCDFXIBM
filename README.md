## LARKY
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

## 5. **Getting started** (Step-by-step instructions to install the required software and how to run a demo of your solution)

## 6. **What your team used to build your solution** (e.g. IBM Cloudant, IBM Cloud Functions, etc...)
IBM Watson Machine Learning instance.

IBM Cloud Annotations for localisation and detection.

IBM Cloud Object Storage for storing data used to train our machine learning model.

Firebase Cloud storage for image data to be uploaded to

## *Items marked with an asterisk are compulsory
