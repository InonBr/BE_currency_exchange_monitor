FROM python:3.8.3-buster

RUN pip install --upgrade pip

COPY  requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /monitor_service

EXPOSE 8002

CMD ["python3", "alerts_monitor_service.py"]