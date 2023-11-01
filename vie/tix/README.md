# Tix

Tix is a computer vision module that will focus on image segmentation, OCR, natural language processing.
This will be the core engine behind taking a page from my scrapbook and turning it into a structured json.

A ticket representation consists of the following properties:

- a unique identifier for the ticket
- reference file for the image
- the bounding box information for the ticket
- title
- location
- date

Tix will three two potential input sources:

1. an image containing multiple tix that will need to be segmented
2. screenshot of ticket from Apple Wallet and Google Wallet
3. email containing ticket info

## SEG.py

SEG is a submodule that provides an abstraction on top of different segmentation options. The default for now will be [SegmentAnything](https://github.com/facebookresearch/segment-anything).
Other options I'm considering are Keras and PyTorch. These will require building the model myself or using the model with a tutorial of the library. First step will be to get the submodule to work then iterate on it.

## OCR.py

OCR is a submodule that provides an abstraction on top of different OCR options. The default for now will be Tesseract.
[Tesseract](https://github.com/tesseract-ocr/tesseract) is an open-source library conceived at HP then later supported at Google.
There are two supported implementations I'm considering using, [PyTesseract](https://github.com/madmaze/pytesseract) and [Tesseract.js](https://github.com/naptha/tesseract.js).

For now, I will be using the PyTesseract library and supporting a backend that is Python-based. This also requires that you install the Tesseract binary:

`brew install tesseract`

Things Under consideration:

- How much of my project should be done in Javascript and how much in Python?
  - Python has the machine learning libraries, image segmentation libraries, and most of the computationally intensive libraries I'll be needing.
  - Maybe prototype all I need with a standard Python backend and then see if there are equivalents in JS?
  - Front-end will likely be done in Javascript
    - Mostly just user interactions
    - Responsible for accessing the data model for manipulation

## NLP.py

NLP is a submodule that provides an abstraction on top of possibly different NLP options. The default for now will be GPT4All. Some options to consider would be ChatGPT, LLaMA, and Bard.

The core need for this submodule is to extract title, location, and date of the event. 

Additional support for building different profiles based on the collection of tickets.

- Hiker
- Live music goer
- Museum enthusiast
