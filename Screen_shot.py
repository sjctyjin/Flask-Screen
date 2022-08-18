import flask
import pyscreenshot as ImageGrab
from io import BytesIO
import time
import win32gui
import win32api
import cv2
import numpy as np

app = flask.Flask(__name__)


def gen():
    while True:
        ps = win32api.GetCursorPos()
        img_buffer = BytesIO()

        #
        # Set childprocess False to improve performance, but then conflicts are possible.
        # ImageGrab.grab(backend='mss', childprocess=True).save(img_buffer, 'PNG', quality=50)
        ImageGrab.grab(backend='mss', childprocess=False).save(img_buffer, 'JPEG', quality=70)
        # print(np.array(img_buffer.getvalue()))
        # img = cv2.imdecode(np.fromfile(os.path.join(path, file), dtype=np.uint8), cv2.IMREAD_UNCHANGED)

        img = cv2.imdecode(np.frombuffer(img_buffer.getvalue(),np.uint8), cv2.IMREAD_UNCHANGED)
        cv2.circle(img, ps, 5, (0,0,255), -1)

        # cv2.imshow("Haha", img)
        # img = cv2.imdecode(img_buffer.getvalue(), cv2.IMREAD_UNCHANGED)
        # cv2.imshow("Haha", img)
        # cv2.waitKey(0)
        flow_img = cv2.imencode('.jpg',img)
        flow_buffer = bytearray(flow_img[1])
        print()
        # yield (b'--frame\r\n'
        #       b'Content-Type: image/png\r\n\r\n' + img_buffer.getvalue() + b'\r\n\r\n')
        yield (b'--frame\r\n'
               # b'Content-Type: image/jpeg\r\n\r\n' + img_buffer.getvalue() + b'\r\n\r\n')
               b'Content-Type: image/jpeg\r\n\r\n' + flow_buffer + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return flask.Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return flask.render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)