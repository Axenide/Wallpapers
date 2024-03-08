import os
from PIL import Image

def resize_images(folder_path, target_height):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):  
            source_filepath = os.path.join(folder_path, filename)
            dest_filepath = os.path.join(os.getcwd(), filename)
            if os.path.exists(dest_filepath):
                print(f"La imagen {filename} ya existe en el directorio actual. No se procesará.")
            else:
                try:
                    img = Image.open(source_filepath)
                    ratio = target_height / float(img.size[1])
                    new_width = int(float(img.size[0]) * ratio)
                    resized_img = img.resize((new_width, target_height))
                    resized_img.save(dest_filepath)
                    print(f"Imagen {filename} redimensionada exitosamente y guardada en el directorio actual.")
                except Exception as e:
                    print(f"Error al procesar la imagen {filename}: {e}")

if __name__ == "__main__":
    folder_path = os.path.dirname(os.getcwd())
    target_height = 300
    resize_images(folder_path, target_height)
