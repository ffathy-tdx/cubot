import cv2
import numpy as np

def detect_face_colors(image_path):
    image = cv2.imread(image_path)
    processed_image = preprocess_image(image)
    face_colors = extract_face_colors(processed_image)
    return face_colors

def preprocess_image(image):
    resized_image = cv2.resize(image, (300, 300))
    processed_image = resized_image

    return image

def extract_face_colors(image):
    color_ranges = {
    'O': (0, 128, 255),    # Orange
    'R': (0, 0, 255),      # Red
    'W': (255, 255, 255),  # White
    'G': (0, 255, 0),      # Green
    'B': (255, 0, 0),      # Blue
    'Y': (0, 255, 255)     # Yellow
}


    #convert to lab
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    face_colors = ''
    # image to 3x3 grid cells and calculate the average color for each cell
    height, width, _ = image.shape
    cell_height = height // 3
    cell_width = width // 3

    for i in range(3):
        for j in range(3):
            #pos
            x_start = i * cell_width
            x_end = (i + 1) * cell_width
            y_start = j * cell_height
            y_end = (j + 1) * cell_height

            #current cell from the lab image
            cell = image[y_start:y_end, x_start:x_end, :]

            average_color = np.mean(cell, axis=(0, 1))

            #closest matching color range
            closest_color = min(color_ranges.keys(), key=lambda x: np.linalg.norm(average_color - color_ranges[x]))

            face_colors += closest_color

    return face_colors

def main():
    image_path = './faces/image2.jpg'
    face_colors = detect_face_colors(image_path)
    print("Face colors:", face_colors)

if __name__ == '__main__':
    main()
