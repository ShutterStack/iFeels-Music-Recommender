import cv2
from django.apps import AppConfig
from flask import Flask, render_template, request


class IfeelsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iFeelsApp'


app = Flask(__name__)

# Import the run_inference function
from static import inference

@app.route('/')
def index():
    return render_template('camera.html')

@app.route('/run_inference', methods=['POST'])
def run_inference():
    # Capture an image from the webcam
    _, frame = cv2.CAP_IMAGES.read()
    frame = cv2.flip(frame, 1)

    # Call the run_inference function with the captured image
    result = inference.run_inference(frame)

    return result

if __name__ == '__main__':
    app.run(debug=True)
