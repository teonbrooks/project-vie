import pytesseract
from pathlib import Path
import os.path as op
import os
from PIL import Image
import toml

project_root = Path(op.join(op.expanduser('~'), 'codespace', 'projet-vie'))

data_path = project_root / 'data'
stubs_path = data_path / 'labelling' / 'images' / 'stubs'

text_path = data_path / 'text_extraction'
if not op.exists(text_path):
    os.mkdir(text_path)

collection = list()
for stub in os.listdir(stubs_path):
    image = Image.open(stubs_path / stub)
    stub_text = pytesseract.image_to_string(image)
    text_extraction.append((stub, stub_text))
    text_extraction = {'filename': stub,
                       'description': stub_text}
    collection.append(text_extraction)

toml_collection = {'title': 'Text Extraction',
                   'stubs': collection}
toml.dump(collection, open(text_path / 'stub_text_extraction.toml', 'w'))
