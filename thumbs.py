import os
from PIL import Image

def resize_and_crop_images(folder_path, target_width, target_height):
    thumbnails_folder = os.path.join(folder_path, ".thumbnails")
    if not os.path.exists(thumbnails_folder):
        os.makedirs(thumbnails_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):  
            source_filepath = os.path.join(folder_path, filename)
            dest_filepath = os.path.join(thumbnails_folder, filename)
            if os.path.exists(dest_filepath):
                # print(f"La imagen {filename} ya existe en la carpeta .thumbnails. No se procesará nuevamente.")
                continue
            else:
                try:
                    img = Image.open(source_filepath)
                    img_ratio = img.width / img.height
                    target_ratio = target_width / target_height

                    # Redimensionar la imagen manteniendo la proporción
                    if img_ratio > target_ratio:
                        new_height = target_height
                        new_width = int(new_height * img_ratio)
                    else:
                        new_width = target_width
                        new_height = int(new_width / img_ratio)

                    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Recortar la imagen centrada
                    left = (resized_img.width - target_width) / 2
                    top = (resized_img.height - target_height) / 2
                    right = (resized_img.width + target_width) / 2
                    bottom = (resized_img.height + target_height) / 2

                    cropped_img = resized_img.crop((left, top, right, bottom))
                    cropped_img.save(dest_filepath)
                    print(f"{filename} procesada y guardada en la carpeta .thumbnails.")
                except Exception as e:
                    print(f"Error al procesar la imagen {filename}: {e}")

if __name__ == "__main__":
    folder_path = os.getcwd()  # Usar la carpeta actual
    target_width = 300
    target_height = 200
    resize_and_crop_images(folder_path, target_width, target_height)
