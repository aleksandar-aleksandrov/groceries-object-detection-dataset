from PIL import Image
import os
import sys
from pathlib import Path

dir = Path(__file__).parent.joinpath('images/tomato_sauce')

for file_name in dir.iterdir():
    print("Processing %s" % file_name)
    image = Image.open(file_name)

    output = image.resize((224, 224), Image.ANTIALIAS)

    output.save(file_name, "PNG", quality = 95)

    print("All done")