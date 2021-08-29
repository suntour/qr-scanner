import os
import config
import re

pattern = re.compile("[a-zA-Z0-9]{3}[-][a-zA-Z0-9]{4}[-][a-zA-Z0-9]{3}[-][a-zA-Z0-9]{3}")

def export(codes):
    output_file = os.path.join(config.get_folder(), config.get_output_file_name())
    with open(output_file, "w") as f:

        print(codes)
        if(codes):
            for code in codes:
                if (validate(code)):
                    f.write(''.join(code) + '\n')
                else:
                    print('Code with invalid format found:' + code)
        else:
            print('There were no codes were scanned')

def validate(code):
    if(pattern.search(code)):
        return True
    return False