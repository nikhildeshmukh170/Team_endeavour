# Technology Stack for Portrait to Landscape Video Converter

---

## Programming Language

- **Python 3.6+**

---

## Libraries & Frameworks

- **OpenCV (opencv-python)**  
  Used for video reading, frame processing, resizing, blurring, and writing the output video.

- **NumPy**  
  Used for efficient numerical operations and array manipulations during video processing.

- **Flask**  
  Lightweight Python web framework to build the web interface for video upload, processing, and playback.

---

## Tools & Utilities

- **pip**  
  Python package installer for managing dependencies.

- **UUID**  
  Python built-in module for generating unique filenames to avoid conflicts.

---

## File Storage

- **Local File System**  
  Stores input uploaded videos in `input/` directory and processed videos in `output/` directory.

---

## Development Environment

- Compatible with Windows, macOS, Linux.
- Virtual environment recommended (`venv` or `virtualenv`).

---

## Optional

- **Browser**  
  Modern browsers like Chrome, Firefox, Edge for accessing the Flask web interface.

---

## Summary

| Component        | Technology          | Purpose                             |
|------------------|---------------------|-----------------------------------|
| Programming      | Python 3.6+         | Core language for backend and processing |
| Video Processing | OpenCV              | Frame manipulation and video output |
| Numerical Ops    | NumPy               | Efficient array operations          |
| Web Framework    | Flask               | Web app and HTTP request handling   |
| Package Manager  | pip                 | Dependency management               |
| Unique Filenames | uuid                | Avoid filename collisions           |
| Storage          | Local filesystem    | Input/output video storage          |

---

## Installation

Use the requirements file:

```bash
pip install -r requirements.txt
