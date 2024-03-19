import os
from PIL import Image

def resize_images(folder_path, target_height):
    thumbnails_folder = os.path.join(folder_path, ".thumbnails")
    if not os.path.exists(thumbnails_folder):
        os.makedirs(thumbnails_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):  
            source_filepath = os.path.join(folder_path, filename)
            dest_filepath = os.path.join(thumbnails_folder, filename)
            if os.path.exists(dest_filepath):
                print(f"La imagen {filename} ya existe en la carpeta .thumbnails. No se procesará nuevamente.")
            else:
                try:
                    img = Image.open(source_filepath)
                    ratio = target_height / float(img.size[1])
                    new_width = int(float(img.size[0]) * ratio)
                    resized_img = img.resize((new_width, target_height))
                    resized_img.save(dest_filepath)
                    print(f"Imagen {filename} redimensionada exitosamente y guardada en la carpeta .thumbnails.")
                except Exception as e:
                    print(f"Error al procesar la imagen {filename}: {e}")

if __name__ == "__main__":
    folder_path = os.getcwd()  # Usar la carpeta actual
    target_height = 300
    resize_images(folder_path, target_height)
