# Architecture Diagram - Portrait to Landscape Video Converter

```plaintext
+--------------------+
|   User Interface   |
|  (Web Browser)     |
|                    |
| - Upload video     |
| - Show loading     |
| - Play output video|
+---------+----------+
          |
          | HTTP POST /process (video upload)
          |
+---------v----------+
|   Flask Web Server |
|                    |
| - Receive video    |
| - Save to input/   |
| - Call Video       |
|   Processing func  |
| - Return HTML with |
|   video player    |
+---------+----------+
          |
          | Calls
          |
+---------v----------+
| Video Processing   |
| (process_portrait_ |
|  to_landscape)     |
|                    |
| - Read input video |
| - Resize & blur    |
| - Compose frames   |
| - Write output     |
|   video to output/ |
+--------------------+

---

## Explanation

1. **User Interface:**  
   Users interact with a simple web page to upload their portrait videos. While the server processes the video, a loading message is shown. Once finished, the processed video is playable directly on the page.

2. **Flask Web Server:**  
   The backend Flask app handles uploads, saves files, triggers the video processing, and serves the processed videos and HTML pages.

3. **Video Processing:**  
   This module uses OpenCV to convert the vertical portrait video into a landscape format by resizing frames, adding a blurred background, and saving the output video.

---

Save this as `architecture_diagram.md` and include it in your project documentation!
