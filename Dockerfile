# Get ubuntu 20.04 #
FROM ubuntu:20.04 

# Update repositories and get the packages needed
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential libssl-dev \
    wget
    git

# Download and install CMAKE 3.20.0 #
RUN cd /opt \
    && wget https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0.tar.gz \
    && tar -zxvf cmake-3.20.0.tar.gz \
    && cd cmake-3.20.0 \
    && ./bootstrap \
    && make \
    && make install

# Donwload and install GROMACS #
RUN cd /opt \
    && git clone -b hugo https://github.com/hugolui/gromacs-mo833a.git \
    && cd gromacs-mo833a \
    && mkdir build \
    && cd build \
    && cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON \
    && make \
    && make check \
    && make install 

# Update path environment variable for GROMACS
RUN echo "source /usr/local/gromacs/bin/GMXRC" >> ~/.bashrc


