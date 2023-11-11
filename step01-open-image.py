#pip install opencv-python
import cv2

image_path = "images/0.jpg"

image = cv2.imread(image_path)

cv2.imshow("Image", image)
cv2.waitKey(6000)
cv2.destroyAllWindows()