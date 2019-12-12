from PIL import Image
import os
import sys
from pathlib import Path

dir = Path(__file__).parent.joinpath('images/fish')

for file_name in dir.iterdir():
    print("Processing %s" % file_name)
    image = Image.open(file_name)

    output = image.resize((224, 224), Image.ANTIALIAS)

    #output_file_name = os.path.join(dir, "small_" + file_name)
    output.save(file_name, "PNG", quality = 95)

    print("All done")