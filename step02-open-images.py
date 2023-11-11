import cv2
import os

folder = "images"
num_images = len(os.listdir(folder))

for i in range(num_images):
    image = cv2.imread(f"{folder}/{i}.jpg")
    cv2.imshow(f"{i}", image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()