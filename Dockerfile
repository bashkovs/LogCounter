FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ./get_weights.sh

EXPOSE 5005

CMD ["python", "app.py"]