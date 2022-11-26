# Importar la biblioteca OpenCV
import cv2

# Definir un objeto de captura de video
import cv2
vid = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
   
    # Capturar el video cuadro por cuadro
    ret, frame = vid.read()

    # Mostrar el cuadro resultante 
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
       roi_color=frame[y:y+h,x:x+w]
       cv2.imwrite("face.jpg",roi_color)

    cv2.imshow("Camera.mp4", frame) # OpenCV no acepta caracteres especiales como el acento en "Cámara"
    
    # Salir de la ventana a través de la barra espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, liberar el objeto capturado
vid.release()

# Destruir todas las ventanas
cv2.destroyAllWindows()