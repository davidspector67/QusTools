# Quantitative Ultrasound Tool

## Overview

This program supports spectral tissue characterization analysis on 2D radiofrequency (RF) and in-phase and quadrature phase (IQ) data.

Additionally, it supports 2D and 3D contrast-enhanced ultrasound (CEUS) analysis for bolus injections. The 2D software uses motion correction software developed by [Thodsawit Tiyarattanachai MD, PhD](https://pubmed.ncbi.nlm.nih.gov/35970658/). Currently, the 3D software does not have motion correction software, but enables users to manually edit their time intensity curve (TIC) as shown in the tutorial below.

## Building

### Mac/Linux

```shell
git clone https://github.com/davidspector67/QusTools.git
cd QusTools
pip install virtualenv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd Parsers
gcc -c -Wall -Wpedantic philips_rf_parser.c
gcc -o philips_rf_parser philips_rf_parser.o
cd ..
```

### Windows

```shell
git clone https://github.com/davidspector67/QusTools.git
cd QusTools
pip install virtualenv
python -m venv venv
call \venv\scripts\activate.bat
pip install -r requirements.txt
deactivate
```

From here, compiler Parser\philips_rf_parser.c into Parser\philips_rf_parser executable using preferred C compiler.

## Running

### Mac/Linux

```shell
source venv/bin/activate
python main.py
deactivate
```

### Windows

```shell
call venv\scripts\activate.bat
python main.py
deactivate
```
