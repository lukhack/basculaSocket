import eventlet
import socketio

sio = socketio.Server(async_mode='eventlet')

app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html', 'origin':'*'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.on('echo')
def echo(sid, message):
    sio.emit('echo', message)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

def worker2():
    while(1):
        print("send clock")
        sio.emit('clock', '1 sec')
        sio.sleep(1)

if __name__ == '__main__':
    sio.start_background_task(worker2)
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)