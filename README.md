# Batch 1 Graduation Photos

## Photo Upload Instructions

Normal GitHub workflow for contributing to a project:

1. Fork repository at the top right
1. Go to your fork
1. Add a **squared** photo of yourself to the region folder you're currently in, with the file name as your name and pod number (for example `europe/eddie-jaoude-1.2.3.jpg`, **note: name in lowercase**)
1. Make a PR for your changes
1. Then... *Relax*!

Any questions raise an issue and one of us can help

## Cropping Instructions

Set up a Python 3 virtual environment
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run
```
python circle-crop.py
```