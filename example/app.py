from flask import Flask, render_template
from flask_serial import Serial
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

import json

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SERIAL_TIMEOUT'] = 0.1
app.config['SERIAL_PORT'] = 'COM1'
app.config['SERIAL_BAUDRATE'] = 115200
app.config['SERIAL_BYTESIZE'] = 8
app.config['SERIAL_PARITY'] = 'N'
app.config['SERIAL_STOPBITS'] = 1

ser = Serial(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send')
def handle_send(json_str):
    data = json.loads(json_str)
    ser.on_send(data['message'])
    print("send to serial: %s"%data['message'])

@ser.on_message()
def handle_message(msg):
    print("receive a message:", msg)
    socketio.emit("serial_message", data={"message":str(msg)})

@ser.on_log()
def handle_logging(level, info):
    print(level, info)

if __name__ == '__main__':
    # Warning!!!
    # this must use `debug=False`
    # if you use `debug=True`,it will open serial twice, it will open serial failed!!!
    socketio.run(app, debug=False)