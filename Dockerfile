# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el script en el contenedor
COPY menu.py /app/menu.py

# Comando para ejecutar el script
CMD ["python", "menu.py"]
