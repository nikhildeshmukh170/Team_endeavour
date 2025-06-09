import cv2
import numpy as np

def process_portrait_to_landscape(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise ValueError("❌ Failed to open input video.")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    input_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    input_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_w = input_h * 16 // 9
    output_h = input_h

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (output_w, output_h))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        portrait_new_w = int((output_h / input_h) * input_w)
        portrait_resized = cv2.resize(frame, (portrait_new_w, output_h))

        bg_blur = cv2.resize(frame, (output_w, output_h))
        bg_blur = cv2.GaussianBlur(bg_blur, (51, 51), 0)

        x_offset = (output_w - portrait_new_w) // 2
        bg_blur[:, x_offset:x_offset + portrait_new_w] = portrait_resized

        out.write(bg_blur)

    cap.release()
    out.release()

    print(f"✅ Landscape video saved to: {output_path}")
