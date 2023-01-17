import pyrebase
config ={
    "apiKey": "AIzaSyBHbuoEVLkgWwVxE47wwAFbWU54S8LzSL4",

  "authDomain": "esp32bloomhehe.firebaseapp.com",

  "databaseURL": "https://esp32bloomhehe-default-rtdb.asia-southeast1.firebasedatabase.app",

  "projectId": "esp32bloomhehe",

  "storageBucket": "esp32bloomhehe.appspot.com",

  "messagingSenderId": "350436147941",

  "appId": "1:350436147941:web:579f6285c1e8e56cdeca0c"

    }
firebase = pyrebase.initialize_app(config)
database = firebase.database()
data = {"Age":21,"Name":"Emily","Likes Pizza":True}

def firesender(datatobesent):
   
    #creating data
    #database.push(data)
    #database.child("Users").child("Firstperson").set(data)

    #reading data
    #emily = database.child("Users").child("Firstperson").get()
    #print(emily.val())

    #how to update data
    database.update({"bloom":datatobesent})

    #removing data
    #deleting one value
    #database.child("Users").child("Firstperson").child("Age").remove()

    #deleting a whole node 
    #database.child("Users").child("Firstperson").remove()