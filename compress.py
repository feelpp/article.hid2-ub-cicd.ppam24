from PIL import Image
import os


def compress_images(directory, quality=85):
    if not os.path.exists(directory):
        print("Directory does not exist")
        return

    output_directory = os.path.join(directory, "compressed")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img = Image.open(os.path.join(directory, filename))
            img.save(os.path.join(output_directory, filename),
                     "JPEG", quality=quality)
        elif filename.endswith(".png"):
            img = Image.open(os.path.join(directory, filename))
            img.save(os.path.join(output_directory, filename),
                     "PNG", optimize=True, quality=quality)

    print(f"Images compressed and saved to {output_directory}")


directory = 'images'
compress_images(directory,quality=50)
