import cv2
import os

image_path = "images/0.jpg"  # Assumindo o nome do arquivo, mas pode ser qualquer extensão

# Verificando a extensão do arquivo
_, file_extension = os.path.splitext(image_path)

# Lista de extensões válidas
valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]

if file_extension.lower() in valid_extensions:
    image = cv2.imread(image_path)
    if image is None:
        print("Erro ao abrir a imagem.")
    else:
        cv2.imshow("Image", image)
        cv2.waitKey(6000)
        cv2.destroyAllWindows()
else:
    print("Formato de arquivo não suportado.")
