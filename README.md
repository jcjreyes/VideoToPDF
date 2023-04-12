<!--toc:start-->

- [MP4 to PDF](#mp4-to-pdf)
  - [Installation and Usage](#installation-and-usage)
    - [Args](#args)
  - [Todo](#todo)
  <!--toc:end-->

# MP4 to PDF

This Python script allows you to convert lecture videos in MP4 format into a series of JPG images.
It uses the OpenCV library to read frames from the video file and save them as individual images.

## Installation and Usage

1. Create a virtual environment using your preferred method
2. Download pip modules

```python
pip install -r requirements.txt
python src.main "FILE.mp4"
```

### Args

1. `-i`, `--interval`
2. `-o`, `--output`

## Todo

- [ ] do the Actual converting into PDF...
- [ ] allow user to select which time they want
- [ ] parallelization? (gpt says concurrent.futures so whatever)
- [ ] progress bar
- [ ] error handling
