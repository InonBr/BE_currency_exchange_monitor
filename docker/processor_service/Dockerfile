FROM python:3.8.3-buster

RUN pip install --upgrade pip

COPY  requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /src

EXPOSE 8001

CMD ["python3", "data_processor_service.py"]