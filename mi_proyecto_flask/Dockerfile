#imagen base oficial de Python
FROM python:3.9-slim


WORKDIR /app


RUN pip install flask

# Copia el contenido del proyecto en el directorio de trabajo
COPY . .

# Exponer puerto
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]
