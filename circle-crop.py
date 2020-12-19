import os
import glob

from PIL import Image, ImageDraw


def crop(region):
    try:
        os.remove(f"{region}/README.md")
    except FileNotFoundError:
        pass

    images = get_images(region)

    try:
        os.mkdir(f"cropped/{region}")
        print(f"Created cropped/{region} directory")
    except FileExistsError:
        print(f"cropped/{region} directory already exists - overwriting existing photos")
    

    print("Cropping")
    
    for image in images:
        crop_image(image)


def get_images(region):
    images = []

    print(f"Collecting photos for {region}")

    images.extend(glob.glob(f"{region}/*"))
    
    print(f"{len(images)} photos collected")
    return images


def crop_image(image):
    img = Image.open(image)

    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse([0, 0, img.size[0], img.size[1]], fill=255)

    img_cropped = img.copy()
    img_cropped.putalpha(mask)

    img_cropped.save(f"cropped/{os.path.splitext(image)[0]}.png")


if __name__ == "__main__":
    try:
        os.mkdir(f"cropped")
        print(f"Created cropped directory")
    except FileExistsError:
        print(f"cropped directory already exists")
    
    regions = ("africa", "asia", "australia-nz", "europe", "middle-east", "north-america", "south-america")

    for region in regions:
        crop(region)
