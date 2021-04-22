#!/bin/bash

cd ../../
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DGMX_BUILD_OWN_FFTW=ON
make
make install
