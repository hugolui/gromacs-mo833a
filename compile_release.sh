#!/bin/bash

mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DGMX_BUILD_OWN_FFTW=ON
make
make install
source /usr/local/gromacs/bin/GMXRC
