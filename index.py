import os
from PIL import Image

# 获取当前日期
import datetime
now = datetime.datetime.now()
current_date = now.strftime("%Y%m%d")

# 输入文件夹和输出文件夹路径
input_folder = "./input/"
output_folder = "./output/"

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def resize_and_convert_image(input_path, output_path):
    try:
        print(f"processing {input_path}")
        img = Image.open(input_path)
        img.save(output_path, "webp", quality=80)
        img.close()
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    # 清空output文件夹
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # 获取当前文件夹中的图片文件
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.webp'))]

    # 处理图片并输出到output文件夹
    processed_count = 0
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_file_name = f"{current_date}{str(processed_count + 1).zfill(3)}.webp"
        output_path = os.path.join(output_folder, output_file_name)
        resize_and_convert_image(input_path, output_path)
        processed_count += 1

    # 清理input文件夹
    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    main()
