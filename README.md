# qr-code-scanner
This program is a more reliable scanner than my other [tesseract-ocr code card scanner](https://github.com/suntour/code-card-scanner).

It uses [opencv](https://pypi.org/project/opencv-python/) to handle the camera feed and decode QR codes from the feed.

# Requirements
[opencv](https://pypi.org/project/opencv-python/)

# Running the program
First, update the `output_folder` and `output_file_name`.

Then run: `python main.py`

# Troubleshooting
If you have more than one camera installed, or your camera feed is not working, you may need to change the `camera_index` value in `config.py`.
Run `python find_cameras.py` to find all camera indices on your system.
