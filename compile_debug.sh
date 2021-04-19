#!/bin/bash

mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Debug -DGMX_BUILD_OWN_FFTW=ON
make
make install
