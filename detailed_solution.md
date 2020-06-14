## Software Framework
1. We used IBM Cloud Annotations to train a model to identify lit kitchen hobs in kitchens. Required service connections to other IBM Services such as IBM Watson Machine Learning instance and IBM Cloud Object Storage.
2. After downloading the model from IBM Cloud Annotations, the model is used in a Python script(#NAME) to classify images taken by a camera. Another Python script(#NAME) is used to automate the taking of pictures every 1 minute.
3. Next, another Python script(#NAME) handles the upload of the images and data to Firebase Cloud Storage.
4. Our frontend will be a Web UI based on Python Django, although it is not implemented yet.
5. A Python script(#NAME) will handle the downloading of data from Firebase Cloud Storage, which will then be displayed via the Web UI.
6. We intend to utilise the network of CCTV and other small cameras placed in strategic/critical locations to monitor areas, and the Web UI will provide real-time updates on each camera.

## Hardware Architecture
1. All CCTVs and other cameras will be connected to a central server using a small plugin device. The central server hosts the Python scripts that will control the camera.
2. The central server will then be connected to the Internet to access Firebase.
3. Web UI will be hosted on a cloud server, either a service from IBM or Firebase.
