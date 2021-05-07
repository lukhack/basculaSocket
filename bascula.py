from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import time
import requests

# Initializing the flask object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('basculaPeso', namespace='/')
def handle_my_custom_namespace_event(json):
    #print('received json: ' + str(json))
    #socketio.emit('basculaPeso', {'data': 42})
    some_function()

@socketio.on("connect", namespace="/")
def connect():
    pass
    # global variable as it needs to be shared
    #global clients
    # emits a message with the user count anytime someone connects
    #some_function()
    #socketio.emit('basculaPeso', {'data': 42})

def some_function():
    while True:
        x = requests.get('http://192.168.1.41/get_var.cgi?index=99')
        data = x.json()['value']
        peso = x = data.split("|")[6]
        #print("peso: "+peso)
        socketio.emit('basculaPeso', {'peso': peso})
        time.sleep(1.1)
# If you are running it using python <filename> then below command will be used
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10001)


