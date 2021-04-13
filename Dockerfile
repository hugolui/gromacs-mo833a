# Get ubuntu 20.04 #
FROM ubuntu:20.04 

# Update repositories and get the packages needed
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential libssl-dev \
    wget

# Download and install CMAKE 3.20.0 #
RUN cd /opt \
    && wget https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0.tar.gz \
    && tar -zxvf cmake-3.20.0.tar.gz \
    && cd cmake-3.20.0 \
    && ./bootstrap \
    && make \
    && make install




