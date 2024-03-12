import numpy as np
import pandas as pd
from pathlib import Path
import os.path as op

project_root = Path(op.join(op.expanduser('~'), 'codespace', 'projet-vie'))


def backend_sam(ndarray):
    from segment_anything import SamAutomaticMaskGenerator, sam_model_registry

    sam = sam_model_registry["default"](checkpoint= project_root / "vie" / 
                                        "_utils" / "sam_vit_h_4b8939.pth" )
    
    # general code, returns "mps" on my system
    # currently not working because of the floating point problem
    # device = "cuda" if torch.cuda.is_available() else "mps" if torch.has_mps else "cpu"
    # sam.to(device=device)
    sam.to('cpu')
    mask_generator = SamAutomaticMaskGenerator(sam)
    masks = mask_generator.generate(ndarray)

    return masks

def segment_collection(filename_collection, start=None, stop=None,
                       backend='segment_anything', device = "cuda"):

    if op.splitext(filename_collection) == '.pdf':
        import pdf2image

        collection = pdf2image.convert_from_path(filename_collection,
                                                 first_page=start,
                                                 last_page=stop)
    if backend == 'segment_anything':
        segmentor = backend_sam
    else:
        NotImplemented('Only `segment_anything` has been implemented.')
    
    collection_segments = list()
    for image in collection:
        collection_segments.append(segmentor(image))
    
    return collection_segments



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



plt.figure(figsize=(20,20))
plt.imshow(img)
show_anns(temp)
plt.axis('off')
plt.show() 

plt.imshow()

# https://keras.io/guides/keras_cv/object_detection_keras_cv/
# could use pretrain module in keras for segmentation