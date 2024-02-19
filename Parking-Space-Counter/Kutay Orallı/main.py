import cv2
import pickle
import numpy as np

cap = cv2.VideoCapture("carPark.mp4")

w, h = 107, 48

with open("car_park_pos", "rb") as f:
    pos_list = pickle.load(f)


def check_parking_space(img_free):
    global color, thickness
    spaces = 0
    totals = 0
    filled = 0
    for pos in pos_list:
        x, y = pos
        totals += 1
        source = img_free[y:y + h, x:x + w]
        count = cv2.countNonZero(source)
        cv2.putText(img, str(count), (x, y + h - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

        if count > 1000:
            color = (0, 255, 0)
            thickness = 5
            filled = + 1
        else:
            color = (0, 0, 255)
            thickness = 3
            spaces += 1
        cv2.rectangle(img, pos, (pos[0] + w, pos[1] + h), color, thickness)

    cv2.rectangle(img, (40, 20), (480, 60), (0, 0, 0), -1)
    cv2.putText(img, f"Total Empty Space: {spaces - filled}/{totals}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 255, 255), 2, cv2.LINE_AA)


while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    # Changing BGR color format to GRAY format

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Adding GaussianBlur for reducing noise

    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)

    # Adding AdaptiveThreshold

    img_threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

    # Median Blur with the ksize 5

    img_median = cv2.medianBlur(img_threshold, 5)

    # Adding kernel unit

    kernel = np.ones((3, 3), np.uint8)

    # Dilates the image one time

    img_dilate = cv2.dilate(img_median, kernel, iterations=1)

    check_parking_space(img_dilate)

    cv2.imshow('Car Parking Lot', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
