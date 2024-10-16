from multiprocessing import Pool
from PIL import Image
import os

def resize_image(image_path):
    img = Image.open(image_path)
    img.resize((800,600))
    img.save(f"resized_{os.path.basename(image_path)}")
    print(f"Processed {image_path}")

if __name__ == '__main--':
    image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    with Pool() as pool:
        pool.map(resize_image,image_paths)