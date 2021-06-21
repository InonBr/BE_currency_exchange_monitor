FROM python:3.8.3-buster

RUN pip install --upgrade pip

COPY  requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /alerts_monitor_service

EXPOSE 8003

CMD ["python3", "zzzzzz.py"]