FROM python:3.8
RUN apt update
RUN apt install -y python3 python3-dev python3-pip

WORKDIR /app
ADD backend/. /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "server.py"]