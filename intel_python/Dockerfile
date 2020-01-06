FROM ubuntu:20.04
LABEL Author="Israel G. de Oliveira" email="prof.israel@gmail.com" Description="For use Intel Python" Version="1.0"

# Install miniconda, from: https://hub.docker.com/r/conda/miniconda3/dockerfile
RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes

ENV PATH /opt/conda/bin:$PATH

# Install Intel Python, from: https://hub.docker.com/r/intelpython/intelpython3_core/dockerfile
ENV ACCEPT_INTEL_PYTHON_EULA=yes

RUN conda config --add channels intel\
    && conda install  -y -q intelpython3_core=2019.4 python=3 \
    && conda clean --all \
    && apt-get update -qqq \
    && apt-get install -y -q g++ \
    && apt-get autoremove

# custom modules and pkgs

RUN apt-get update && apt-get install -y \
  wget \
  htop \
  vim \
  jed \
  nano \
  dos2unix

COPY /requirements.txt /requirements.txt

RUN conda config --add channels conda-forge
RUN conda config --add channels bioconda 
RUN conda install --file requirements.txt

# For supermarkdown:
RUN conda install jupyter_contrib_nbextensions qgrid RISE  
RUN jupyter contrib nbextension install
RUN jupyter nbextension enable --py --sys-prefix qgrid
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix

RUN mkdir /work

COPY /servers.sh /servers.sh

WORKDIR /work

EXPOSE 8888

CMD ["/servers.sh"]