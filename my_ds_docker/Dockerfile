FROM python:3.7-buster

RUN apt-get update && apt-get install -y \
  wget \
  htop \
  vim \
  jed \
  nano \
  dos2unix

RUN pip install -U pip

COPY /requirements.txt /requirements.txt

RUN pip install -r requirements.txt

# For supermarkdown:
RUN pip install jupyter_contrib_nbextensions qgrid RISE  
RUN jupyter contrib nbextension install
RUN jupyter nbextension enable --py --sys-prefix qgrid
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix

RUN mkdir /work

COPY /servers.sh /servers.sh

WORKDIR /work

EXPOSE 8888 8501

CMD ["/servers.sh"]

#EOF