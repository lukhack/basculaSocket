from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import time

# Initializing the flask object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('getSomeData', namespace='/')
def handle_my_custom_namespace_event(json):
    print('received json: ' + str(json))
    socketio.emit('getSomeData', {'data': 42})

@socketio.on("connect", namespace="/")
def connect():
    # global variable as it needs to be shared
    #global clients
    # emits a message with the user count anytime someone connects
    #some_function()
    socketio.emit('getSomeData', {'data': 42})

def some_function():
    while True:
        print("datos")
        socketio.emit('getSomeData', {'data': 42})
        time.sleep(1)
# If you are running it using python <filename> then below command will be used
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10001)


