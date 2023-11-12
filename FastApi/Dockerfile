FROM python:3.8

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /FastAPI

COPY ./app /FastAPI/app

# Instala las dependencias desde el archivo requirements.txt
COPY ./requirements.txt /FastAPI
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]
