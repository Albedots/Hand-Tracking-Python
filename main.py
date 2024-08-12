# importação das bibliotecas
import cv2
from cvzone.HandTrackingModule import HandDetector

# inicializa a webcam
webcam = cv2.VideoCapture(0)
# inicializa o rastreador de mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

# loop infinito para sempre estar capturando imagens e gerar um video
while True:
    sucesso, imagem = webcam.read() # captura a imagem da webcam
    coordenadas, imagens_maos = rastreador.findHands(imagem) # detecta as mãos no quadro

    print(coordenadas) # mostra as coordenadas das mãos no terminal

    cv2.imshow("Projeto IA", imagens_maos) # mostra os quadros com a marcação do tracking

    if cv2.waitKey(1) != -1: # encerra a aplicação quando qualquer tecla é pressionada
        break

# libera a câmera e fecha as janelas 
webcam.release()
cv2.destroyAllWindows()