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



while True:
    
    time.sleep(5)
    print("Uploading image now..")
    path_on_cloud = "images/location_1.png"
    path_local = "location_1.png"
    storage.child(path_on_cloud).put(path_local)
    print("Image uploaded. System will sleep for x seconds before uploading next image")

