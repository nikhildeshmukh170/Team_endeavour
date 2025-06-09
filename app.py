from flask import Flask, request, send_file, jsonify, url_for
import os
import uuid
from src.video_crop import process_portrait_to_landscape

app = Flask(__name__)

UPLOAD_FOLDER = 'input'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Portrait to Landscape Video Converter</title>
        <style>
            * { box-sizing: border-box; }
            body {
                background: #f4f7fa;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: flex-start;
                min-height: 100vh;
                margin: 0;
                padding: 40px 20px;
                color: #333;
            }
            .container {
                background: white;
                padding: 30px 40px;
                border-radius: 12px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.1);
                width: 100%;
                max-width: 700px;
                text-align: center;
            }
            h1 {
                margin-bottom: 25px;
                color: #2c3e50;
            }
            input[type="file"] {
                padding: 10px;
                border-radius: 6px;
                border: 1px solid #ccc;
                font-size: 16px;
                width: 100%;
                max-width: 350px;
                cursor: pointer;
            }
            button {
                margin-top: 20px;
                background: #3498db;
                border: none;
                color: white;
                padding: 12px 28px;
                font-size: 18px;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.3s ease;
                width: 100%;
                max-width: 350px;
            }
            button:hover {
                background: #2980b9;
            }
            #loading {
                margin-top: 30px;
                font-size: 18px;
                color: #2980b9;
                display: none;
                justify-content: center;
                align-items: center;
                gap: 12px;
            }
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #3498db;
                border-radius: 50%;
                width: 28px;
                height: 28px;
                animation: spin 1s linear infinite;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            #result {
                margin-top: 40px;
            }
            a.download-link {
                display: inline-block;
                margin-bottom: 20px;
                font-size: 18px;
                color: #27ae60;
                text-decoration: none;
                font-weight: 600;
            }
            a.download-link:hover {
                text-decoration: underline;
            }
            video {
                max-width: 100%;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            }
            @media (max-width: 480px) {
                .container {
                    padding: 20px;
                }
                button, input[type="file"] {
                    max-width: 100%;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Upload Portrait Video</h1>
            <form id="uploadForm" enctype="multipart/form-data">
                <input type="file" name="video" accept="video/*" required />
                <br />
                <button type="submit">Upload and Convert</button>
            </form>
            <div id="loading"><div class="spinner"></div> Processing video, please wait...</div>
            <div id="result"></div>
        </div>

        <script>
            const form = document.getElementById('uploadForm');
            const loading = document.getElementById('loading');
            const result = document.getElementById('result');

            form.addEventListener('submit', async (e) => {
                e.preventDefault();
                result.innerHTML = '';
                loading.style.display = 'flex';

                const formData = new FormData(form);

                try {
                    const response = await fetch('/process_async', {
                        method: 'POST',
                        body: formData
                    });

                    if (!response.ok) {
                        const text = await response.text();
                        throw new Error(text);
                    }

                    const data = await response.json();
                    loading.style.display = 'none';

                    result.innerHTML = `
                        <h2 style="color: #27ae60;">✅ Video Processed Successfully!</h2>
                        <a class="download-link" href="${data.download_url}" download>⬇️ Download Processed Video</a>
                        <br />
                        <video controls playsinline preload="metadata" width="640" style="max-width: 100%;">
                            <source src="${data.download_url}" type="video/mp4" />
                            Your browser does not support the video tag.
                        </video>
                        <br />
                        <a href="/" style="margin-top: 25px; display: inline-block; color: #3498db; font-weight: 600; text-decoration: none;">Upload Another Video</a>
                    `;
                } catch (err) {
                    loading.style.display = 'none';
                    result.innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
                }
            });
        </script>
    </body>
    </html>
    '''

@app.route('/process_async', methods=['POST'])
def process_video_async():
    file = request.files.get('video')
    if not file:
        return 'No file uploaded.', 400

    input_filename = f"{uuid.uuid4()}.mp4"
    output_filename = f"{uuid.uuid4()}_landscape.mp4"
    input_path = os.path.join(UPLOAD_FOLDER, input_filename)
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    file.save(input_path)
    print(f"[INFO] Saved input video to: {input_path} (size: {os.path.getsize(input_path)} bytes)")

    try:
        process_portrait_to_landscape(input_path, output_path)
        print(f"[INFO] Processed output video to: {output_path}")
    except Exception as e:
        print(f"[ERROR] Video processing failed: {e}")
        return f'Error processing video: {e}', 500

    if not os.path.exists(output_path):
        print("[ERROR] Processed video file not found after processing.")
        return 'Processed video file not found.', 500

    size = os.path.getsize(output_path)
    print(f"[INFO] Output video size: {size} bytes")
    if size == 0:
        print("[ERROR] Processed video file is empty.")
        return 'Processed video file is empty.', 500

    download_url = url_for('download_file', filename=output_filename)
    return jsonify({'download_url': download_url})

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    print(f"[INFO] Serving video file: {filepath}")
    if not os.path.exists(filepath):
        print("[ERROR] File not found:", filepath)
        return "File not found", 404
    return send_file(filepath, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
