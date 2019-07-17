# flask-serial
receive and send data of serial in Flask

xx
# install

- download:

    `git clone https://github.com/RedFalsh/flask-serial.git`

- install:

    `python setup.py install`
    
# pip install

`pip install flask-serial`  

# Usage

```python

from flask import Flask
from flask_serial import Serial

app = Flask(__name__)
app.config['SERIAL_TIMEOUT'] = 0.2
app.config['SERIAL_PORT'] = 'COM2'
app.config['SERIAL_BAUDRATE'] = 115200
app.config['SERIAL_BYTESIZE'] = 8
app.config['SERIAL_PARITY'] = 'N'
app.config['SERIAL_STOPBITS'] = 1


ser =Serial(app)

@app.route('/')
def use_serial():
    return 'use flask serial!'

@ser.on_message()
def handle_message(msg):
    print("receive a message:", msg)
    # send a msg of str
    ser.on_send("send a str message!!!")
    # send a msg of bytes
    ser.on_send(b'send a bytes message!!!')

@ser.on_log()
def handle_logging(level, info):
    print(level, info)

if __name__ == '__main__':
    app.run()
    
```

# Use With Socketio 

```python

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
    
    
```

