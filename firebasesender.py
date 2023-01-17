import pyrebase
def firesender(datatobesent):
    config ={
    "apiKey": "AIzaSyBZyf4pJK6uhvxZjEGyMDVi79ldAa-Ve1U",
    "authDomain": "fir-esp32-demo-fc4c0.firebaseapp.com",
    "databaseURL": "https://fir-esp32-demo-fc4c0-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "fir-esp32-demo-fc4c0",
    "storageBucket": "fir-esp32-demo-fc4c0.appspot.com",
    "messagingSenderId": "1032001540500",
    "appId": "1:1032001540500:web:081e507a99bcac97d7ff81"
    }
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    data = {"Age":21,"Name":"Emily","Likes Pizza":True}

    #creating data
    #database.push(data)
    #database.child("Users").child("Firstperson").set(data)

    #reading data
    #emily = database.child("Users").child("Firstperson").get()
    #print(emily.val())

    #how to update data
    database.child("test").update({"int":str(datatobesent)})

    #removing data
    #deleting one value
    #database.child("Users").child("Firstperson").child("Age").remove()

    #deleting a whole node 
    #database.child("Users").child("Firstperson").remove()