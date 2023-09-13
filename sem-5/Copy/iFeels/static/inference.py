import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model

# Load your model and labels
model = load_model("model.h5")
label = np.load("labels.npy")

def run_inference(image):
    lst = []

    # Process the image with Mediapipe
    res = holis.process(image)

    if res.face_landmarks:
        for i in res.face_landmarks.landmark:
            lst.append(i.x - res.face_landmarks.landmark[1].x)
            lst.append(i.y - res.face_landmarks.landmark[1].y)

        if res.left_hand_landmarks:
            for i in res.left_hand_landmarks.landmark:
                lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
        else:
            for _ in range(42):
                lst.append(0.0)

        if res.right_hand_landmarks:
            for i in res.right_hand_landmarks.landmark:
                lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
        else:
            for _ in range(42):
                lst.append(0.0)

        lst = np.array(lst).reshape(1, -1)

        pred = label[np.argmax(model.predict(lst))]

        return pred

# Initialize Mediapipe and other necessary components
holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils
