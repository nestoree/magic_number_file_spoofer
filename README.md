# Magic Number File Spoofer (Python)

Este script en Python permite añadir magic numbers (file signatures) a un archivo existente para que aparente ser de otro tipo de archivo, independientemente de su extensión original.

---

## ⚠️ Importante:
Este script NO convierte realmente el contenido del archivo.
Solo añade la firma mágica al inicio, lo que puede engañar a detecciones básicas basadas únicamente en headers.

---

## 📌 ¿Qué son los magic numbers?

Los magic numbers (o file signatures) son secuencias de bytes al inicio de un archivo que indican su tipo real (PNG, JPG, PDF, ZIP, etc.).

Ejemplos:

PNG → 89 50 4E 47 0D 0A 1A 0A
JPG → FF D8 FF
PDF → %PDF
ZIP → 50 4B 03 04

Muchos sistemas utilizan estos bytes para identificar archivos, no la extensión.

---

## 🧠 ¿Para qué sirve este script?

- Aprender cómo funcionan las firmas de archivos
- Análisis forense
- Seguridad y validación de uploads
- Pruebas de detección basadas en headers
- Entornos Linux / servidores

---

## 🚀 Funcionamiento

El script:

Pide un archivo de entrada (ej. hello.php)
Permite elegir un tipo de archivo objetivo (PNG, JPG, PDF, etc.)
Inserta el magic number correspondiente al inicio
Guarda un nuevo archivo modificado

---

## 🧩 Tipos de archivo soportados

- PNG
- JPG
- GIF
- PDF
- ZIP
(Se pueden añadir más fácilmente en el código)

---

## 🛠️ Requisitos

Python 3.6 o superior
No requiere librerías externas

---

## ▶️ Uso

Ejecuta el script:
'''
python magic_spoofer.py
'''

📄 Ejemplo práctico

Archivo original:
'''
hello.php
'''

Contenido real:
'''
<?php echo "Hola mundo"; ?>
'''

Resultado:
'''
imagen.png
'''

➡️ El archivo puede ser detectado como PNG por herramientas básicas, aunque el contenido sigue siendo PHP.

---

## ⚠️ Advertencia ética y legal

Este proyecto es exclusivamente educativo.

**No** usar para:
- Evasión de seguridad
- Subida de archivos maliciosos
- Engaño de sistemas productivos
- El autor no se hace responsable del mal uso del script.

---

## 📜 Licencia

MIT License
Uso libre con fines educativos.
