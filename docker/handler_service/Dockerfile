FROM python:3.8.3-buster

RUN pip install --upgrade pip

COPY  requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /src

EXPOSE 8003

CMD ["python3", "alerts_handler_service.py"]