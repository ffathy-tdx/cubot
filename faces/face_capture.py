import cv2

def capture_image(camera_index, save_directory):
    capture = cv2.VideoCapture(camera_index)

    if not capture.isOpened():
        print("Failed to open camera")
        return

    ret, frame = capture.read()

    if not ret:
        print("Failed to capture frame")
        return

    save_path = save_directory + "/captured_image.jpg"

    cv2.imwrite(save_path, frame)

    capture.release()

camera_index = 3
save_directory = "./"

capture_image(camera_index, save_directory)
print("n")