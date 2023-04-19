import os
import img2pdf


class ImageToPdfConverter:
    def __init__(self, image_dir, pdf_file):
        self.image_dir = image_dir
        self.pdf_file = pdf_file

    def find_files(self):
        files = []
        for filename in os.listdir(self.image_dir):
            if filename.endswith('.png') and filename[:-4].isdigit():
                files.append(filename)
        files.sort(key=lambda x: int(x[:-4]))
        return files

    def convert(self):
        files = self.find_files()
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(files))
