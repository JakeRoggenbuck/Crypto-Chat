from firebase import firebase

def send(text, name):
    db = firebase.FirebaseApplication('https://python-firebase-39b0a.firebaseio.com', None)
    string = [name, text]
    result = db.post('/messages', string)

def recive():
    db = firebase.FirebaseApplication('https://python-firebase-39b0a.firebaseio.com', None)
    return db.get('/messages', None)

