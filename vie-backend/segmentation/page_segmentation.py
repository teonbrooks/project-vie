import pandas as pd
from pathlib import Path
import os.path as op
import os
from PIL import Image

project_root = Path(op.join(op.expanduser('~'), 'codespace', 'projet-vie'))

data_path = project_root / 'data' / 'labelling'
images = os.listdir(data_path / 'images')

stubs_path = data_path / 'images' / 'stubs'
if not op.exists(stubs_path):
    os.mkdir(stubs_path)

def yolobbox2bbox(x,y,w,h):
    x1, y1 = x-w/2, y-h/2
    x2, y2 = x+w/2, y+h/2
    return x1, y1, x2, y2

for image in images:
    file, ext = op.splitext(image)
    bboxes = pd.read_csv(op.join(data_path, 'labels', file + '.txt'), 
                         delimiter=' ', names = ['type', 'x', 'y', 'w', 'h'])
    img = Image.open(data_path / 'images' / image)
    x, y = img.size
    # The YOLO bbox is scaled to one. Need to rescale for PIL
    bboxes[['x', 'w']] *= x
    bboxes[['y', 'h']] *= y
    for ii, bbox in bboxes.iterrows():
        # convert from YOLO to two-point bbox
        bbox = yolobbox2bbox(**bbox[['x', 'y', 'w', 'h']])
        cropped = img.crop(bbox)
        cropped.save(stubs_path / f'{file}-stub_{ii:02d}.jpg')