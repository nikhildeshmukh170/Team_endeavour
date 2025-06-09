#Team_Endeavour

# Portrait to Landscape Video Converter

This project converts a portrait-oriented video to a landscape video by adding a blurred background and centering the portrait frame. This is especially useful for displaying portrait videos on landscape screens.

---

## 📸 Overview

- Upload a portrait video.
- The application processes the video and saves a landscape version with a blurred background.
- Download and play the processed video.

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/portrait-to-landscape-video.git
   cd portrait-to-landscape-video
   ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Flask app**
    ```bash
    python app.py
    ```
5. **Open your browser and go to:**
    ```bash
    http://127.0.0.1:5000/
    ```
6. **Upload a portrait video and get the processed landscape video with blurred background.**


🛠️ How It Works
Reads input portrait video frame-by-frame.

Calculates output landscape width for a 16:9 aspect ratio.

Resizes each frame to fit the new width, preserving height.

Creates a blurred background from the original frame.

Places the resized frame centered on the blurred background.

Writes the processed frames to a new MP4 video file.

📂 **Project Structure:**

```bash
.
├── app.py                       # Flask web application
├── requirements.txt             # Project dependencies
├── src/
│   └── video_crop.py            # Video processing logic
└── README.md                    # Project documentation
```

👨‍💻 **Authors**

Nikhil Deshmukh — e22cseu1099@bennett.edu.in

Piyanshu Saini — e22cseu1280@bennett.edu.in