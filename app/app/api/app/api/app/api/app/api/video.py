import cv2

def process_video(file):
    # Replace with your custom video processing logic
    cap = cv2.VideoCapture(file.file)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return f"Extracted {len(frames)} frames"
