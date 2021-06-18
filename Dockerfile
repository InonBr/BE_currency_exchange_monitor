FROM python:3.8.3-buster

RUN pip install --upgrade pip

COPY  docker/py_data_processor_service/requirements.txt .

RUN pip install -r ./requirements.txt

COPY src /src

WORKDIR /src

EXPOSE 80

CMD ["python", "data_processor_service.py"]
