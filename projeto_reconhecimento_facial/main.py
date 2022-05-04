import cv2 #opencv
import mediapipe as mp

#inicializar opencv e o mediapipe
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_de_rosto = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solution.drawing_utils

while True:
    #ler informaçoes da webcam
    verificador, frame = webcam.read()
    if not verificador:
        break
    #reconhecer os rostos que tem na imagem
    lista_rostos = reconhecedor_de_rosto.process(frame)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            #desenhar os rostos na imagem
            desenho.draw_detection(frame, rosto)

    cv2.imshow("janela", frame)

    if cv2.waitKey(5) == 27:
        break
    #quando apertar esc, para o loop
webcam.release()