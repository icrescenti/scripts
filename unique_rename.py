import os
from pathlib import Path
from datetime import datetime

for index, path in enumerate(Path('mypath').rglob('*.png')):
    os.rename(path, 'done/' + datetime.now().strftime("%Y%m%d%H%M%S%f") + str(index) + '.png')