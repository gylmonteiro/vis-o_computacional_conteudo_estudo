import cv2
import os

folder = "images"
num_images = len(os.listdir(folder))

for i in range(num_images):
    image = cv2.imread(f"{folder}/{i}.jpg")
    if image is None:
        print(f"Erro: Não foi possivel abrir a imagem {i}.jpg")
        exit()

    cv2.namedWindow("Imagem", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Imagem", cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Imagem", image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()