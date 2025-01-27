import cv2
import os

# Ruta del video
video_path = "videos/h6923828e_M1391V069_4K.mov"

# Verificar si el archivo existe
if not os.path.exists(video_path):
    print(f"❌ ERROR: El archivo '{video_path}' no existe. Verifica la ruta y vuelve a intentarlo.")
    exit()

# Capturar video desde archivo
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"❌ ERROR: No se pudo abrir el archivo de video: {video_path}")
    exit()

# Crear background subtractor para detectar movimiento
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40, detectShadows=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    mask = subtractor.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mascara - Movimiento Detectado", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

