FROM python:3.8.3-buster
RUN pip install --upgrade pip
COPY  requirements.txt . 
RUN pip install -r ./requirements.txt



#RUN mkdir /app
#WORKDIR /app
#COPY src .
#
#
#
#
#CMD ["python", "main.py"]
