import cv2
import os

# Ruta del video
video_path = "videos/h6923828e_M1391V069_4K.mov"

# Verificar si el archivo existe
if not os.path.exists(video_path):
    print(f"❌ ERROR: El archivo '{video_path}' no existe. Verifica la ruta y vuelve a intentarlo.")
else:
    print(f"✅ Archivo encontrado: {video_path}")

# Intentar abrir el video con OpenCV
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"❌ ERROR: No se pudo abrir el archivo de video: {video_path}")
    print("🔹 Soluciones posibles:")
    print("  1️⃣ Asegúrate de que el archivo esté en la carpeta correcta.")
    print("  2️⃣ Prueba con una ruta absoluta en lugar de relativa.")
    print("  3️⃣ Convierte el archivo a .mp4 si sigue sin funcionar.")
else:
    print(f"✅ OpenCV pudo abrir el video correctamente.")

# Cerrar el archivo de video
cap.release()
