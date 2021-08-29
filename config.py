output_folder = r"C:\Users\USER_NAME\Desktop\test_folder"
output_file_name = r"codes.txt"
camera_index = 0 #You may need to change this value, run py find_cameras.py to find all camera indexes to try
pattern = "[a-zA-Z0-9]{3}[-][a-zA-Z0-9]{4}[-][a-zA-Z0-9]{3}[-][a-zA-Z0-9]{3}"

def get_folder():
    return output_folder

def get_output_file_name():
    return output_file_name

def get_pattern():
    return pattern

def get_camera_index():
    return camera_index