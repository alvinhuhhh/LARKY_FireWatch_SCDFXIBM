import pyrebase
import time



config = {
    "apiKey": "AIzaSyBJjY8hLlzt2QcI5aUwojGt0z38fQ6Eofs",
    "authDomain": "ibmxscdf.firebaseapp.com",
    "databaseURL": "https://ibmxscdf.firebaseio.com",
    "projectId": "ibmxscdf",
    "storageBucket": "ibmxscdf.appspot.com",
    "messagingSenderId": "32797032290",
    "appId": "1:32797032290:web:91c2276551ce15070d363b",
    "measurementId": "G-WMLW7XK5CY"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

print("Starting script..")

while True:
    
    
    print("Uploading image now..") 
    path_on_cloud = "images/location_1.png" 
    path_local = "location_1.png"
    storage.child(path_on_cloud).put(path_local) #upload the image file to Firebase cloud
    print("Image uploaded!")
    
    print("Uploading status now..")
    path_on_cloud = "images/status_1.txt"
    path_local = "status_1.txt"
    storage.child(path_on_cloud).put(path_local) #upload the status file to Firebase cloud
    print("Status uploaded!")
    
    print("All files uploaded. System will sleep for 60 seconds before uploading next file")
    
    time.sleep(60)

