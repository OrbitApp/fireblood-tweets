
from firebase import firebase
import json
import ast

import ast
u = "u{'code1':1,'code2':1}"
d = ast.literal_eval(u"{'code1':1,'code2':1}")

def on_data():
    # print data
    # json_string = json.dumps(data)

    #new_data = data.text
    nd = {"a": "b"}
    firebase1 = firebase.FirebaseApplication('https://mydd-d1223.firebaseio.com/', None)
    result = firebase1.post('/tweets', nd)
    return True

#on_data()
#print json.code1
print d["code1"]

