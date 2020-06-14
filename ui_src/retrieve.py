import pyrebase
import time
import os


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



while True:
    
    
    print("Starting files download now..")
    i = 1
    
    while i != 0:
       
        
        path_on_cloud = "images/status_" + str(i) + ".txt"
        
        print("Getting status..")
  
        storage.child(path_on_cloud).download("", "status_" + str(i) + ".txt")
        
        STATUS_FILE_PATH = "status_" + str(i) + ".txt"
        PHOTO_FILE_PATH = "location_" + str(i) + ".png"
        
        
        
        f = open(STATUS_FILE_PATH, "r")
        
        j = f.read()
        
        
        
        if int(j) == 1:
            print("Fire detected in photo.. Downloading image")
        
       
        
            path_on_cloud = "images/location_" + str(i) + ".png"
  
            storage.child(path_on_cloud).download("", "location_" + str(i) + ".png")
            
            print("Image downloaded.. System will sleep for 10 seconds before next update..")
        else:
            if os.path.exists(PHOTO_FILE_PATH):
                os.remove(PHOTO_FILE_PATH)
        
            print("No fire detected.. System will sleep for 10 seconds before next update..")
       
        i -= 1
    
    time.sleep(10)
    
