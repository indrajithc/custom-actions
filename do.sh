#!/bin/bash

file=$1
name="${file%.*}"
python -m PyQt5.uic.pyuic -x $file -o "$name.py"
python "$name.py"
