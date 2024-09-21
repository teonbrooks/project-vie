import pickle
import numpy as np
from pathlib import Path
import os.path as op
import pdf2image


project_root = Path(op.join(op.expanduser('~'), 'codespace', 'projet-vie'))
filename_collection = project_root / 'data' / 'source' / 'scrapbook.pdf'

# this is to load the scrapbook pdf
collection = pdf2image.convert_from_path(filename_collection)
for ii, FILE in enumerate(collection):
    FILE.save(project_root / 'data' / 'source' / f'scrapbook_{ii:02d}.jpg')
