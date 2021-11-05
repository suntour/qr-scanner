# qr-code-scanner
This program is a more reliable scanner than my other [tesseract-ocr code card scanner](https://github.com/suntour/code-card-scanner).

![image](https://user-images.githubusercontent.com/37424999/140589277-a4d4b6ea-4988-48ca-b8bd-701008a6ba19.png)

It uses [opencv](https://pypi.org/project/opencv-python/) to handle the camera feed and decode QR codes from the feed.

# Requirements
[opencv](https://pypi.org/project/opencv-python/)

# Running the program
First, update the `output_folder` and `output_file_name`.

Then run: `python main.py`

When the square is purple, it means the QR code has not been added to the list yet.

Move on to the next card when the square turns green (it should be near instant).

# Troubleshooting
If you have more than one camera installed, or your camera feed is not working, you may need to change the `camera_index` value in `config.py`.

Run `python find_cameras.py` to find all camera indices on your system.
