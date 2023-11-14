FROM ubuntu:22.04

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install libglib2.0-0 libgl1 libsm6 libxext6  -y
RUN apt-get -y install python3-pip python3
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN ./get_weights.sh

EXPOSE 5005

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5005"]