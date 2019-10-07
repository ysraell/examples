FROM python:buster

RUN apt-get update && apt-get install -y \
  wget \
  htop \
  vim \
  jed \
  nano

RUN pip install -U pip

COPY /requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /work

COPY /servers.sh /servers.sh

WORKDIR /work

EXPOSE 8888 8501

CMD ["/servers.sh"]

