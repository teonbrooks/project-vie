import pickle
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import numpy as np
from pathlib import Path
import os.path as op
import pdf2image


project_root = Path(op.join(op.expanduser('~'), 'codespace', 'projet-vie'))
filename_collection = project_root / 'data' / 'scrapbook.pdf'

# this is to load the scrapbook pdf
collection = pdf2image.convert_from_path(filename_collection)[-1]

# this creates the segmentation 
sam = sam_model_registry["default"](checkpoint= project_root / "vie" / 
                                    "_utils" / "sam_vit_h_4b8939.pth" )
sam.to(device='mps')

mask_generator = SamAutomaticMaskGenerator(sam)
masks = mask_generator.generate(np.array(collection))
pickle.dump(open('/Users/teonbrooks/Desktop/mask_ultimate', 'wb'))

def show_anns(anns):
    if len(anns) == 0:
        return
    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    img = np.ones((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 4))
    img[:,:,3] = 0
    for ann in sorted_anns:
        m = ann['segmentation']
        color_mask = np.concatenate([np.random.random(3), [0.35]])
        img[m] = color_mask
    ax.imshow(img)

# plt.figure(figsize=(20,20))
plt.imshow(collection.convert('L'), cmap='gray', vmin=0, vmax=255)
show_anns(temp)
plt.axis('off')
plt.show() 

plt.imshow()