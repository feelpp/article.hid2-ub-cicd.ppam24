from PIL import Image
import os


def resize_and_compress_images(directory, max_width, max_height, quality=85):
    if not os.path.exists(directory):
        print("Directory does not exist")
        return

    output_directory = os.path.join(directory, "processed")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        print(f"Processing {filename}")
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            img_path = os.path.join(directory, filename)
            with Image.open(img_path) as img:
                # Calculate the new size preserving the aspect ratio
                img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
                # Save the processed image
                if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                    img.save(os.path.join(output_directory, filename),
                             "JPEG", quality=quality)
                elif filename.endswith(".png"):
                    img.save(os.path.join(output_directory, filename),
                             "PNG", optimize=True, quality=quality)

    print(f"Images resized and compressed, saved to {output_directory}")


# Set the directory path to your image folder
directory = 'images'
# Set the maximum width and height for the images (in pixels)
max_width = 595  # A4 width in points (1 point = 1/72 inch)
max_height = 842  # A4 height in points

resize_and_compress_images(directory, max_width, max_height)
