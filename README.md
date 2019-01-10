# flask-serial
receive and send data of serial in Flask

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
