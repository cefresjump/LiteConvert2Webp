import os
from PIL import Image

def convert_to_webp(input_path, output_path, max_size):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(input_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, os.path.splitext(filename)[0] + ".webp")

            img = Image.open(input_file)

            # Compress the image until it's below the desired maximum size
            quality = 90  # Starting quality value
            while True:
                img.save(output_file, format="webp", quality=quality)
                if os.path.getsize(output_file) < max_size:
                    break
                quality -= 5  # Decrease the quality if the file size is still too large

            print(f"Converted {filename} to WebP format with quality {quality}.")

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    max_file_size_bytes = 1024 * 1024  # 1MB

    convert_to_webp(input_folder, output_folder, max_file_size_bytes)
