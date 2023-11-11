
import cv2
import numpy as np

# Carregue o modelo
net = cv2.dnn_DetectionModel('frozen_inference_graph.pb', 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Carregue a lista de nomes das classes
with open('coco.names', 'rt') as f:
    names = f.read().rstrip('\n').split('\n')

# Abra o fluxo de vídeo da webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,960)

while True:
    # Capture frame-by-frame
    ret, img = cap.read()

    if not ret:
        break

    height, width, channels = img.shape

    # Realize a detecção
    class_ids, confidences, boxes = net.detect(img, confThreshold=0.4, nmsThreshold=0.2)

    # Crie uma máscara toda preta (zeros) do tamanho da imagem
    mask = np.zeros((height, width, 3), dtype=np.uint8)

    # Crie uma lista de cores
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 0, 255)]
    color_idx = 0

    for class_id, confidence, box in zip(class_ids.flatten(), confidences.flatten(), boxes):
        if confidence > 0.50:
            if names[class_id-1] == 'pessoa':  # verifique se o objeto detectado é uma pessoa
                left, top, width, height = box
                current_color = colors[color_idx % len(colors)]
                mask[top:top+height, left:left+width] = current_color  # atribua a cor atual à área da pessoa detectada
                color_idx += 1

    # Mesclar a máscara colorida com a imagem original
    alpha = 0.5  # quanto da máscara colorida você quer misturar com a imagem original
    img = cv2.addWeighted(mask, alpha, img, 1 - alpha, 0)

    # Mostre a imagem
    cv2.imshow('Detecção', img)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Quando tudo estiver concluído, libere a captura
cap.release()
cv2.destroyAllWindows()
