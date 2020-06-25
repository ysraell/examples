# PoC: Boost Python

To make all work:
```bash
$ wget https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.tar.bz2 && tar xfjv eigen-3.3.7.tar.bz2 && rm eigen-3.3.7.tar.bz2
$ mv eigen-3.3.7 /usr/local/
$ apt-get update && apt-get install -y \
    curl libboost-python-dev libboost-dev \
    build-essential zlib1g-dev libboost-system-dev \
    libboost-program-options-dev 
```

**WIP**.
